from sqlwrapper import gensql, dbget,dbput
import datetime
import json

def HOTEL_AR_POST_SELECT_AccountPostHistory(request):
    invoice_no = request.json['invoice_no']
    result = json.loads(dbget("select employee.emp_firstname,account_posting_history.* \
                               from account_receivable.account_posting_history \
                               left join reservation.employee on employee.emp_id = account_posting_history.acc_user_id \
                               where invoice_id = '"+str(invoice_no)+"'"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def HOTEL_AR_POST_SELECT_AccountPayHistory(request):
    
    invoice_no = request.json['account_no']

    result = json.loads(dbget("select payment_code.payment_code,payment_code.payment_type,account_pay_history.* \
                              from account_receivable.account_pay_history \
                              left join cashiering.payment_code on payment_code.payment_code_id = account_pay_history.payment_type_id \
                              where account_pay_history.account_no = '"+str(invoice_no)+"'"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def HOTEL_AR_POST_SELECT_ApplyPaymentSelectiviely(request):
    d =request.json
    Posting_date = datetime.datetime.utcnow().date()
    s = {}
    
    account_invoie = json.loads(dbget("select open_amount from account_receivable.accout_inivoice \
                                       where account_number = '"+str(d['account_no'])+"' and invoice_no = '"+str(d['invoice_no'])+"'"))
    
    acc_inv = account_invoie[0]['open_amount'] - d['posting_amount']
    print(acc_inv)

    acc_set = json.loads(dbget("select account_balance from account_receivable.account_setup \
                                       where account_number = '"+str(d['account_no'])+"'"))
    setupamount = acc_set[0]['account_balance'] - d['posting_amount']
    d['posting_date'] = Posting_date
    d['posting_status'] = "Apply Payment Selectively"
    gensql('insert','account_receivable.invoice_payment',d)
    
    sql = dbput("update account_receivable.account_setup set account_balance = '"+str(setupamount)+"' \
                    where account_number = '"+d['account_no']+"'")
    psql = dbput("update account_receivable.accout_inivoice set open_amount = '"+str(acc_inv)+"' \
                 where account_number = '"+d['account_no']+"' and invoice_no = '"+str(d['invoice_no'])+"' ")
    s['invoice_id'] = str(d['invoice_no'])
    s['account_no'] = d['account_no']
    s['payment_type_id'] = d['payment_code_id']
    s['post_date'] = Posting_date
    s['payment_amount'] = d['posting_amount']
   
    gensql('insert','account_receivable.account_pay_history',s)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))

    
def HOTEL_AR_POST_INSERT_UNApplyPayment(request):
    d = request.json
    Posting_date = datetime.datetime.utcnow().date()
    s = {}
    
    account_invoie = json.loads(dbget("select open_amount from account_receivable.accout_inivoice \
                                       where account_number = '"+str(d['account_no'])+"' and invoice_no = '"+str(d['invoice_no'])+"'"))
    
    acc_inv = account_invoie[0]['open_amount'] + d['posting_amount']
    print(acc_inv)

    acc_set = json.loads(dbget("select account_balance from account_receivable.account_setup \
                                       where account_number = '"+str(d['account_no'])+"'"))
    setupamount = acc_set[0]['account_balance'] + d['posting_amount']
    a = { k : v for k,v in d.items() if v != '' if k not in ('account_no','invoice_no','posting_payment_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('account_no','invoice_no','posting_payment_id')}
    print(e)
    a['posting_date'] = Posting_date
    a['posting_status'] = "UnApply"
    a['posting_amount'] = '-'+str(d['posting_amount'])
    gensql('update','account_receivable.invoice_payment',a,e)

    sql = dbput("update account_receivable.account_setup set account_balance = '"+str(setupamount)+"' \
                    where account_number = '"+d['account_no']+"'")
    print(sql)
    psql = dbput("update account_receivable.accout_inivoice set open_amount = '"+str(acc_inv)+"' \
                 where account_number = '"+d['account_no']+"' and invoice_no = '"+str(d['invoice_no'])+"' ")
    
    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                       "Status": "Success","StatusCode": "200"},indent=4))
def HOTEL_AR_POST_SELECT_ReversePayment(request):
    d = request.json
    Posting_date = datetime.datetime.utcnow().date()
    s = {}
    
    account_invoie = json.loads(dbget("select open_amount from account_receivable.accout_inivoice \
                                       where account_number = '"+str(d['account_no'])+"' and invoice_no = '"+str(d['invoice_no'])+"'"))
    
    acc_inv = account_invoie[0]['open_amount'] + d['posting_amount']
    print(acc_inv)

    acc_set = json.loads(dbget("select account_balance from account_receivable.account_setup \
                                       where account_number = '"+str(d['account_no'])+"'"))
    setupamount = acc_set[0]['account_balance'] + d['posting_amount']
    print(setupamount)
    a = { k : v for k,v in d.items() if v != '' if k not in ('account_no','invoice_no','posting_payment_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('account_no','invoice_no','posting_payment_id')}
    print(e)
    a['posting_date'] = Posting_date
    a['posting_status'] = "Reverse Payment"
    a['posting_amount']=-(d['posting_amount'])
    gensql('update','account_receivable.invoice_payment',a,e)
    sql = dbput("update account_receivable.account_setup set account_balance = '"+str(setupamount)+"' \
                    where account_number = '"+d['account_no']+"'")
    psql = dbput("update account_receivable.accout_inivoice set open_amount = '"+str(acc_inv)+"' \
                 where account_number = '"+d['account_no']+"' and invoice_no = '"+str(d['invoice_no'])+"' ")
    payment = json.loads(dbget("select payment_code_id from account_receivable.invoice_payment \
                               where account_no = '"+d['account_no']+"' and posting_payment_id = '"+str(e['posting_payment_id'])+"'"))
    s['invoice_id'] = str(d['invoice_no'])
    s['account_no'] = d['account_no']
    s['payment_type_id'] = payment[0]['payment_code_id']
    s['post_date'] = Posting_date
    s['payment_amount'] = -(d['posting_amount'])
   
    gensql('insert','account_receivable.account_pay_history',s)
    
    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                       "Status": "Success","StatusCode": "200"},indent=4))

    
def HOTEL_AR_POST_SELECT_UnappyPayment(request):

    acc_no = request.json['account_no']
    inv = request.json['invoice_no']
    Posting_date = datetime.datetime.utcnow().date()
    result = json.loads(dbget("select * from account_receivable.invoice_payment\
                           left join cashiering.payment_code on payment_code.payment_code_id = invoice_payment.payment_code_id \
                           where posting_date = '"+str(Posting_date)+"' and account_no = '"+str(acc_no)+"' and invoice_no = '"+str(inv)+"' "))
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))


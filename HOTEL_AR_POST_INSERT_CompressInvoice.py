from sqlwrapper import gensql, dbget,dbput
import datetime
import json

def HOTEL_AR_POST_INSERT_CompressInvoice(request):
    d = request.json
    s ,z,f= {},[],{}
    print("hello world")
    select = json.loads(dbget("select * from account_receivable.invoice_no"))
    print(select,type(select),len(select))

    invoice_id = (select[0]['invoice_num']+1)
    print(invoice_id)
    update = dbput("update account_receivable.invoice_no set invoice_num = '"+str(select[0]['invoice_num']+1)+"'")
   
    s['invoice_no'] = invoice_id
    s['account_name'] = d['account_name']
    s['account_number'] = d['account_number']
    s['invoice_supplement'] = d['invoice_supplement']
    s['reference'] = d['reference']
    s['market_id'] = d['market_id']
    s['source_id'] = d['source_id']
    s['room_class_id'] = d['room_class_id']
    s['invoice_amount'] = d['invoice_amount']
    s['open_amount'] = d['open_amount']
    s['acc_invoice_satus'] = "New Compress"
    gensql('insert','account_receivable.accout_inivoice',s)
    
    z= d['invoice_no']
    for i in z:
        print(invoice_id,i)
        f['new_invoice_id'] = invoice_id
        f['compress_invoice'] = i
        gensql('insert','account_receivable.account_compress',f)
        sql = dbput("update account_receivable.accout_inivoice set acc_invoice_satus = 'Compress'\
                     where account_number = '"+d['account_number']+"' and invoice_no = '"+str(i)+"'")
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200","invoice_num":invoice_id},indent=4))


def HOTEL_AR_POST_DELETE_UnCompressInvoice(request):

    d = request.json
    z= d['invoice_no']
    
    for i in d['invoice_no']:
  
        sql = dbput("update account_receivable.accout_inivoice set acc_invoice_satus = 'UnCompress' \
                     where account_number = '"+d['account_number']+"' and invoice_no = '"+str(i)+"'")
        print(sql)
        query = json.loads(dbget("select new_invoice_id from account_receivable.account_compress \
                                  where compress_invoice = '"+str(i)+"'"))
        print(query)
        delinvoice = dbput("delete from account_receivable.accout_inivoice where invoice_no = '"+str(query[0]['new_invoice_id'])+"'")
        psql =  dbput("delete from account_receivable.account_compress where compress_invoice = '"+str(i)+"' ")
    return(json.dumps({"Return": "Record Deleted Successfully","ReturnCode": "RDS","Status": "Success","StatusCode": "200"},indent=4))


def HOTEL_AR_POST_SELECT_YearViewAmount(request):
    period_view = []
    yearview = json.loads(dbget("select  invoice_date,open_amount  from account_receivable.accout_inivoice \
                              order by DATE(invoice_date)"))
    print(yearview)

    for i in yearview:
        period = datetime.datetime.strptime(i['invoice_date'],'%Y-%m-%d').date()
        print(period.strftime('%b,%y'))
        period_view.append({'period':period.strftime('%b,%Y'),'Balance':i['open_amount']})
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': period_view  ,'ReturnCode':'RRTS'},indent=4))

 
 
    

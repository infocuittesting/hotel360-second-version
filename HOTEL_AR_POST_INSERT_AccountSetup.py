from sqlwrapper import gensql, dbget,dbput
import datetime
import json

def HOTEL_AR_POST_INSERT_AccountSetup(request):
    d = request.json
    print(d)
    RES_Log_Date = datetime.datetime.utcnow().date()
    #print(RES_Log_Date)
    count_pf_id = json.loads(dbget("select count(*) from account_receivable.account_setup where profile_id='"+d['profile_id']+"' "))
    #print(count_pf_id[0]['count'],type(count_pf_id[0]['count']))
    if count_pf_id[0]['count'] != 0:
       return(json.dumps({"Return": "Record Already Inserted","ReturnCode": "RAI",
                       "Status": "Success","StatusCode": "200"},indent=4))
 
    
    ac_name = json.loads(dbget("select pf_account from profile.pf_company_profile where pf_id='"+d['profile_id']+"' "))
    ac_name = ac_name[0]['pf_account']
    ac = ac_name.split(" ")
    name=''
    for i in ac:
        name+=i[0]
    #print(name)
    ac_no = json.loads(dbget("select ac_no from account_receivable.account_number"))
    
    ac_no1 = str(ac_no[0]['ac_no']+1)
    account_number = name+ac_no1
    #print(account_number)
    dbput("update account_receivable.account_number set ac_no='"+str(ac_no[0]['ac_no']+1)+"' ")
    d['account_number'] = account_number
    d['created_on'] = RES_Log_Date
    d['account_balance']= "0.00"
    gensql('insert','account_receivable.account_setup',d)
    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200","Account_number":account_number},indent=4))


def HOTEL_AR_POST_UPDATE_AccountSetup(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('profile_id','account_number')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('profile_id','account_number')}
    print(e)
    gensql('update','account_receivable.account_setup',a,e)
    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                       "Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_AR_POST_SELECT_AccountSetup(request):

     result = json.loads(dbget('select currency.*, country.*,state.*,pf_company_profile.pf_account,account_type.account_type_id,account_type.account_type,account_type.account_type_description,employee.emp_firstname, account_setup.* from account_receivable.account_setup \
                              left join reservation.employee on employee.emp_id = account_setup.created_by \
                              left join profile.country on country.id = account_setup.country_id \
                              left join profile.state on state.id = account_setup.state_id \
                              left join profile.currency on currency.id = account_setup.currency_id \
                              left join account_receivable.account_type on account_type.account_type_id = account_setup.account_type_id \
                              left join profile.pf_company_profile on pf_company_profile.pf_id = account_setup.profile_id'))
     return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result,'ReturnCode':'RRTS'},indent=4))

def HOTEL_AR_POST_DELETE_AccountSetup(request):    
   pf_id = request.json['profile_id']
   print(pf_id)
   dbput(("delete from account_receivable.account_setup where profile_id = '"+pf_id+"' "))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                      'Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))

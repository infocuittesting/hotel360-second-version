#Input Param: 
#OutputParam: Record Inserted Successfully
#Purpose: This service used for crate company profile
#Date:13/03/2018
#UpdateDate:29/06/2018
#Author: Aravinth

from sqlwrapper import gensql,dbget,dbput
import datetime
import json
def UpdateCompanyProfile(request):
    d = request.json
    select = json.loads(dbget("select * from profile.profile_id"))
    print(select,type(select),len(select))
    print(select[0]['profile_id'])
    id1 = "cpy"+str(select[0]['profile_id']+1)
    print(id1)
    update = dbput("update profile.profile_id set profile_id = '"+str(select[0]['profile_id']+1)+"'")
    d['pf_id'] = id1
    sql_value = gensql('insert','profile.pf_company_profile',d) 

    data1 = d.get("PF_Firstname")
    pf_type = d['PF_Type']
    
    PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    print(PF_Log_Time)
    PF_Log_Date = datetime.datetime.utcnow().date()
    print(PF_Log_Date)
    
    PF_Log_Description = "Create "+str(pf_type)+" Profile" + " "+str(data1)
    s = {}
    s['Emp_Id'] = '121'
    s['Emp_Firstname'] = "daisy"
    s['Emp_Lastname'] = "veroni"
    s['PF_Log_Date'] = PF_Log_Date
    s['PF_Log_Time'] = PF_Log_Time
    s['PF_Action_Type'] = "New Profile"
    s['PF_Log_Description'] = PF_Log_Description
    s['pf_id'] = id1
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)
    # finally return the value from DB_Wrapper   
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','profileid':id1,'profiletype':pf_type,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
def UpdateCompanyProfileRecord(request):
    d = request.json
    PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    print(PF_Log_Time)
    PF_Log_Date = datetime.datetime.utcnow().date()
    #print(d)
    e = { k : v for k,v in d.items() if k in ('PF_Id')}
    f = { k : v for k,v in d.items() if k not in ('PF_Id') if v != ''}
    gensql('update','profile.pf_company_profile',f,e)
    s = {}
    s['Emp_Id'] = '121'
    s['Emp_Firstname'] = "daisy"
    s['Emp_Lastname'] = "veroni"
    s['PF_Log_Date'] = PF_Log_Date
    s['PF_Log_Time'] = PF_Log_Time
    s['PF_Action_Type'] = "Update Profile"
    s['PF_Log_Description'] = "Update profile changes"
    s['pf_id'] = d['PF_Id']
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))    

def UpdateIndividualProfileRecord(request):
    d = request.json
    PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    print(PF_Log_Time)
    PF_Log_Date = datetime.datetime.utcnow().date()
    #print(d)
    e = { k : v for k,v in d.items() if k in ('PF_Id')}
    f = { k : v for k,v in d.items() if k not in ('PF_Id') if v != ''}
    gensql('update','profile.pf_individual_profile',f,e)
    s = {}
    s['Emp_Id'] = '121'
    s['Emp_Firstname'] = "daisy"
    s['Emp_Lastname'] = "veroni"
    s['PF_Log_Date'] = PF_Log_Date
    s['PF_Log_Time'] = PF_Log_Time
    s['PF_Action_Type'] = "Update Profile"
    s['PF_Log_Description'] = "Update profile changes"
    s['pf_id'] = d['PF_Id']
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))    

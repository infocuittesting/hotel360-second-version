from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
import datetime
def UpdateProfilePreferencenew(request):
    PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    print(PF_Log_Time)
    PF_Log_Date = datetime.datetime.utcnow().date()
    d = request.json
    sql_value = gensql('insert','profile.pf_preference',d)
    s = {}
    s['Emp_Id'] = '121'
    s['Emp_Firstname'] = "daisy"
    s['Emp_Lastname'] = "veroni"
    s['PF_Log_Date'] = PF_Log_Date
    s['PF_Log_Time'] = PF_Log_Time
    s['PF_Action_Type'] = "Profile Preference"
    s['PF_Log_Description'] = d['PF_Preference_Group']
    s['pf_id'] = d['pf_id']
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

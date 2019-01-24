import json
import random
from sqlwrapper import gensql,dbget,dbput
import datetime

def HOTEL_BBL_POST_INSERT_GroupCancel(request):

    sql_value = json.loads(dbget("select block_cancel_no from business_block.block_cancel"))
    print(sql_value,type(sql_value))
    
    sql_value1 = sql_value[0]['block_cancel_no']
    print(sql_value1,type(sql_value1))
    count = sql_value1 + 1
    psql = dbput("update business_block.block_cancel set block_cancel_no = '"+str(sql_value[0]['block_cancel_no']+1)+"'")
    d = request.json
    d['cancellation_number'] = count
    print(d)   
    sql = gensql('insert','business_block.group_cancel',d)
    print(sql)
    block_id = d.get("block_id")
    psql = dbput("update business_block.business_block_definite set block_status_id = '5' where block_id = '"+block_id+"'")
    cancelgrid = json.loads(dbget("select count(*) from business_block.grid where block_id= '"+block_id+"' \
	                          union \
	                          select count(*) from business_block.current_grid where block_id= '"+block_id+"' "))
    print(cancelgrid)

    if cancelgrid[0]['count'] > 0:
        deltequery = dbput("delete from business_block.grid where block_id = '"+block_id+"' ; \
                            delete from business_block.current_grid where block_id = '"+block_id+"'")
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    s = {}
    s['user_role'] = "Supervisor"

    s['date'] = RES_Log_Date
    s['time'] = RES_Log_Time
    s['block_id'] = d.get("block_id")
    s['action_type_id'] = "Group Cancelled"
    s['description'] = d.get("cancel_description")
    gensql('insert','business_block.business_block_activity_log',s)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200",'CancellationNumber':count},indent=4))

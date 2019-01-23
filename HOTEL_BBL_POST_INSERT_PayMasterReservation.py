import datetime
from sqlwrapper import gensql, dbget, dbput
import json
def HOTEL_BBL_POST_INSERT_PayMasterReservation(request):
    d = request.json
    x,s = {},{}
    block_id = d.get("block_id")
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)

    psql = json.loads(dbget("select count (*) from reservation.res_reservation where res_block_code='"+block_id+"' and res_room_type in('PM')"))
    #print("sds",psql)
    count = psql[0]['count']
    #print("sfd",type(count),count)
    if psql[0]['count'] > 0:
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Reservation Already Exist','ReturnCode':'RAE'}, sort_keys=True, indent=4)) 

    sql = json.loads(dbget("select start_date,end_date,block_name,nights,pf_id from business_block.business_block_definite where block_id = '"+block_id+"'"))

    startdate = sql[0]['start_date']
    enddate = sql[0]['end_date']
    name = sql[0]['block_name']
    x['res_arrival'] = startdate
    x['res_depature'] = enddate
    x['res_nights'] = sql[0]['nights']
    x['pf_id'] = sql[0]['pf_id']
    x['res_block_code'] = block_id
    x['res_block']=sql[0]['pf_id']
    x['res_guest_status'] = "Definite Block"
    x['res_room_type'] = "PM"
    x['res_number_of_rooms'] = str(1)
    x['created_by'] = "Ranimanagama"
    x['created_on'] = RES_Log_Date
    select = json.loads(dbget("select * from reservation.res_id"))
    print(select,type(select),len(select))
    print(select[0]['id'])
    Res_id = (select[0]['id']+1)
    print(Res_id)
    update = dbput("update reservation.res_id set id = '"+str(select[0]['id']+1)+"'")
    x['Res_id'] = Res_id

    sqlvalue = json.loads(dbget("select confirmation_no from business_block.group_confirmation"))
    print(sqlvalue,type(sqlvalue))
    sqlvalue = int(sqlvalue[0]['confirmation_no'])

        
    confirmation_no = sqlvalue + 1
    print(confirmation_no,type(confirmation_no))
    psql = dbput("update business_block.group_confirmation set confirmation_no = '"+str(confirmation_no)+"'")
    print(psql)
    d['res_confnumber'] = confirmation_no
    psqlvalue = gensql('insert','reservation.res_reservation',x)
    print(psqlvalue)

    s = {}
    s['user_role'] = "Supervisor"
    s['date'] = RES_Log_Date
    s['time'] = RES_Log_Time
    s['block_id'] = block_id
    s['action_type_id'] = "PAY MASTER"
    s['description'] = "Pay Master will be created"+" "+str(name)
    gensql('insert','business_block.business_block_activity_log',s)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
   
def HOTEL_BBL_POST_SELECT_QueryPayMasterReservation(request):
    d = request.json
    block_id = d.get("block_id")
    #psql = json.loads(dbget("select * from reservation.res_reservation where res_block_code = '"+block_id+"' and res_room_type in ('PM')"))
    #print(psql)
    psql = json.loads(dbget("select * from reservation.res_reservation where res_block_code = '"+block_id+"' "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':psql  ,'ReturnCode':'RRTS'},indent=4))
   
    


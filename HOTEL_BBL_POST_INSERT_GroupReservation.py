import datetime
from sqlwrapper import gensql, dbget, dbput
import json
from Hotel_END_OF_Day_POST_countrycheck import HOTEL_REM_POST_SELECT_SelectRateForReservation,get_rate
#from flask import Flask,request, jsonify
#app = Flask(__name__)
#@app.route("/HOTEL_BBL_POST_INSERT_GroupReservations",methods = ['POST'])

def HOTEL_BBL_POST_INSERT_GroupReservation(request):
    
    d = request.json
    #print(d)
    x = {}
    res_block_code = d[0]["res_block_code"]
    #print("hello",res_block_code,type(res_block_code))
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    #print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    #print(RES_Log_Date)
    
    select = json.loads(dbget("select * from reservation.res_id"))
    #print(select,type(select),len(select))
    #print(select[0]['id'])
    Res_id = (select[0]['id']+1)
    #print(Res_id)
    update = dbput("update reservation.res_id set id = '"+str(select[0]['id']+1)+"'")
    
    for w in d:
        #print(w,type(w))
        #editkey = w.get("editFlag")
        #if (editkey == 'false'):
        if 'editFlag' in w:
            
            del w['editFlag']
        x['pf_firstname'] = w.get("pf_firstname")
        select = json.loads(dbget("select * from profile.profile_id"))
        #print(select,type(select),len(select))
        #print(select[0]['profile_id'])
        id1 = "ind"+str(select[0]['profile_id']+1)
        print(id1)
        update = dbput("update profile.profile_id set profile_id = '"+str(select[0]['profile_id']+1)+"'")
        select_data = json.loads(dbget("select \
                                       reservation.market.marketgroup_description,\
                                       business_block_definite.pf_id as companyaccount, \
                          reservation.res_source.sourcedescription,\
                          reservation.origin.origindescription \
    			  from business_block.business_block_definite \
			  left join reservation.market on reservation.market.id = business_block_definite.market_id \
			  left join reservation.res_source on reservation.res_source.id = business_block_definite.source_id \
			  left join reservation.origin on reservation.origin.id = business_block_definite.origin_id \
			  where block_id='"+res_block_code+"' "))
        rate_code_detail = json.loads(dbget("select \
                                          reservation.restype.restype_description,\
                                          revenue_management.ratecode.rate_code as ratecode\
                                          from business_block.block_room \
                                          left join reservation.restype on restype.id = block_room.res_type_id\
			                  left join revenue_management.ratecode on revenue_management.ratecode.ratecode_id = block_room.ratecode_id \
    			                  where block_id='"+res_block_code+"' "))
        
        x['pf_id'] = id1
        x['pf_mobileno']="NA"
        x['pf_lastname']="NA"
        x['pf_mobileno']="0"
        x['pf_type']="Individual"
        x['pf_city']="NA"
        x['pf_postalcode']="0"
        gensql('insert','profile.pf_individual_profile',x)
        w['pf_id'] = id1
        w['res_guest_status'] = "reserved" 
        w['created_by'] = "Ranimanagama"
        w['created_on'] = RES_Log_Date
        w['Res_id'] = Res_id
        w['res_market']= select_data[0]['marketgroup_description']
        w['res_source'] =select_data[0]['sourcedescription']
        w['res_origin']=select_data[0]['origindescription']
        w['res_res_type']=rate_code_detail[0]['restype_description']
        w['res_rate_code']=rate_code_detail[0]['ratecode']
        w['res_block'] = select_data[0]['companyaccount']
        data = HOTEL_REM_POST_SELECT_SelectRateForReservation(w['res_arrival'],w['res_rate_code'],w['res_room_type'],int(w['res_adults']))
         
        w['res_rate']=data
        sqlvalue = json.loads(dbget("select confirmation_no from business_block.group_confirmation"))
        #print(sqlvalue,type(sqlvalue))
        sqlvalue = int(sqlvalue[0]['confirmation_no'])
        confirmation_no = sqlvalue + 1
        #print(confirmation_no,type(confirmation_no))
        psql = dbput("update business_block.group_confirmation set confirmation_no = '"+str(confirmation_no)+"'")
        #print(psql)
        w['res_confnumber'] = confirmation_no
        psqlvalue = gensql('insert','reservation.res_reservation',w)
        #print(psqlvalue)

    s = {}
    s['user_role'] = "Supervisor"
    s['date'] = RES_Log_Date
    s['time'] = RES_Log_Time
    s['block_id'] = res_block_code
    s['action_type_id'] = "Group Reservation"
    s['description'] = "Group Reservation Created Successfully"
    gensql('insert','business_block.business_block_activity_log',s)
        
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
def HOTEL_BBL_POST_SELECT_QueryGroupReservation(request):
    d = request.json
    block_id = d.get("block_id")
    sql_value  = json.loads(dbget("select * from reservation.res_reservation where res_block_code='"+block_id+"' and res_room_type not in('PM') "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
   

   


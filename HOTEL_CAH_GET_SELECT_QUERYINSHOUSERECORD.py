from sqlwrapper import gensql, dbget
import json


def HOTEL_CAH_POST_SELECT_QUERYINHOUSERECORD(request):

    value1 = json.loads(dbget("SELECT * FROM reservation.res_reservation where res_guest_status in ('checkin','due out') "))
    print(value1) 
    value2 = json.loads(dbget("select * from reservation.res_reservation where \
                        CURRENT_DATE between res_arrival and res_depature and res_guest_status='Check out' "))  
    print(value2)
    sql_value = value1+value2
    print(sql_value)

    
       
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))


# select CURRENT_DATE) between res_arrival and res_depature and res_guest_status='Check out'

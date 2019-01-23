from sqlwrapper import gensql, dbget
import json


def HOTEL_CAH_POST_SELECT_QUERYINHOUSERECORD(request):

    value1 = json.loads(dbget("SELECT pf_company_profile.pf_account,res_reservation.* FROM reservation.res_reservation \
                               left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.res_block \
                               where res_reservation.res_guest_status in ('checkin','due out') "))
    print(value1) 
    value2 = json.loads(dbget("select pf_company_profile.pf_account,res_reservation.* from reservation.res_reservation \
                            left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.res_block \
                             where CURRENT_DATE between res_arrival and res_depature and res_guest_status='Check out' "))  
    print(value2)
    sql_value = value1+value2
    print(sql_value)

    
       
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))


# select CURRENT_DATE) between res_arrival and res_depature and res_guest_status='Check out'

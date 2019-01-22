from sqlwrapper import dbget
import json
from HOTEL_REM_POST_SELECT_UpdateRatecodeSetup import HOTEL_REM_POST_SELECT_SelectRatesetupAll
from datetime import datetime, timedelta
import requests
#@app.route("/ProfileFutureReservationRecord",methods=['POST'])
def HOTEL_RES_POST_select_Paticularreservation(request):
    d = request.json
    result = json.loads(dbget("select * from reservation.res_reservation \
         where res_id = '"+str(d['res_id'])+"' and res_unique_id = '"+str(d['res_unique_id'])+"' "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))
def QueryHistoryReservation(request):
    #N = 365
    current_date = datetime.utcnow().date()
    current_date = str(current_date)
    print(current_date)
    #date_N_days_ago = current_date + timedelta(days=1)
    #date_N_days_ago = date_N_days_ago.date()

    #date_N_days_ago = str(date_N_days_ago)
    #print (date_N_days_ago)
    pf_id = request.json['pf_id']
    sql_value = "select * from reservation.res_reservation where pf_id = '"+pf_id+"' and res_arrival <  '"+current_date+"' order by res_arrival desc"
    result = dbget(sql_value)
    #sql_value = gensql('select','reservation.res_reservation','*' 'ORDER BY res_arrival DESC')
    result = json.loads(result)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))

def get_rate(s):
    if s == 4:
        return('four_adult_rate')
    elif s == 3:
        return('three_adult_rate')
    elif s == 2:
        return('two_adult_rate')
    elif s == 1:
        return('one_adult_rate')
        
def HOTEL_RES_POST_SELECT_RateQuery(request):
    
     s = request.json
     rate_code ,ratecode_rooms_id,ratecode_packages_id,result= [],[],[],[]
     #query = requests.post("https://hotel360.herokuapp.com/HOTEL_REM_POST_SELECT_SelectRatesetupAll")
     data = json.loads(HOTEL_REM_POST_SELECT_SelectRatesetupAll(request))
     #print(data)
     #print(type(data['Rate_header']))
     
     list_roomtypes = [ r['r_type'] for r in json.loads(dbget("SELECT type as r_type \
                                        FROM room_management.room_type"))]
     print("list_roomtypes",list_roomtypes)
     records = data['records']
     new_records = []
     #result = [d for d in value[0]['rate_details'] if d['start_date'] <= s['arrival_date'] and d['end_date'] >= s['departure_date']]
     for record in records:
             new_record = {}
             new_record['rate_code'] = record['rate_code']
             #new_records.append(new_record)
             for detail in record['rate_details']:
                 
                if detail['start_date'] <= s['arrival_date'] or detail['end_date'] >= s['departure_date']:
                    '''
                    for rm in detail['rooms']:
                       #print(rm['roomstype'],rm['roomid'])
                       ratecode_packages_id.append(rm['roomstype'])
                       if s['adults'] == 4:
                        rm['rate'] = detail['advanced_details']['four_adult_rate']
                       elif s['adults'] == 3:
                        rm['rate'] = detail['advanced_details']['three_adult_rate']
                       elif s['adults'] == 2:
                        rm['rate'] = detail['advanced_details']['two_adult_rate']
                       elif s['adults'] == 1:
                        rm['rate'] = detail['advanced_details']['one_adult_rate']
                    '''
                    new_record['rates'] = [dict(rm, rate=detail['advanced_details'][get_rate(s['adults'])]) for rm in detail['rooms']]

                    new_rooms = [] 
                    for r_type in new_record['rates']:
                            new_rooms.append(r_type['roomstype'])
                            
                    for list1 in list_roomtypes:
                        if list1 in new_rooms:
                            pass
                        else:
                            new_record['rates'].append({'roomstype':list1,'rate':0})
                          
             new_records.append(new_record)
             
     print("new_records",new_records)        
     #print("roomytpe",set(ratecode_packages_id))
     #final_value = sorted(new_records,key = lambda x: x['rates'] )
     #for new_record in new_records:
     #for l in list_roomtypes:
             #for rm in  new_record['rates']:
                
                    #new_record['rates'].append({'rooms_selected_id':0,'rooms_id':0,'roomid':list_roomtype['id'],'roomstype':list_roomtype['type'],'rate':0})
                 
             #  ratecode_rooms_id.append(d)
             #  print("&&&",ratecode_rooms_id)
     #result = [d for d in value[d]['rate_details'] if d['start_date'] >= s['arrival_date'] and d['end_date'] <= s['departure_date']]
     #print(type(result))
     '''
     for results in result:
         ratecode_rooms_id.append(results['rooms_id'])
         ratecode_packages_id.append(results['packages_id'])
     print(ratecode_rooms_id)
     print(ratecode_packages_id)
     for ratecode_room in ratecode_rooms_id:
         rec1 = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id, room_type.room_type_id,room_type.room_type \
                             from revenue_management.rooms_selected join revenue_management.room_type on \
                             rooms_selected.room_type_id = room_type.room_type_id \
                             where revenue_management.rooms_selected.rooms_id='"+str(ratecode_room)+"'"))
     print(rec1)

     for ratecode_package in ratecode_packages_id:
      rec2 = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id \
                             where revenue_management.packages_selected.packages_id='"+str(ratecode_package)+"'"))
     print(rec2)
     a, b = [],[]
     for results in result:
       #print("results['rooms_id']",results['rooms_id'])
      
       for roomtype in rec1:
     
             #print(roomtype['rooms_selected_id'],results['rooms_id'])
               
             if roomtype['rooms_id'] == results['rooms_id']:
               #print(roomtype['rooms_selected_id'],results['rooms_id'])
               #print(roomtype)
               a.append(roomtype)
             
           
       results['rooms_id'] = a
     for results in result:
         for package in rec2:
             if package['packages_id'] == results['packages_id']:
                    b.append(package)
         results['packages_id'] = b     
     #print("rate", rate_details)
     #return(json.dumps({"Return": result,"Status": "Success","StatusCode": "200"},indent=4))
     for room_details in result:
        rooms = room_details['rooms_id']
        if len(rooms) == 0:
            pass
        else:
            for room in rooms:
               for rate in rate_details:
                  #if room['rooms_id'] == rate['rooms_id']: 
                     if s['adults'] == 4:
                        room['room_rate'] = rate['four_adult_amount']       
                     elif s['adults'] == 3:
                        room['room_rate'] = rate['three_adult_amount']
                     elif s['adults'] == 2:
                         room['room_rate'] = rate['two_adult_amount']
                     elif s['adults'] == 1:
                         room['room_rate'] = rate['one_adult_amount']
     '''
                 
     return(json.dumps({"Return": new_records,"Status": "Success","StatusCode": "200"},indent=4))

import json
from sqlwrapper import gensql,dbput,dbget
import datetime
def GetReservationReport(request):
    
   from_date = request.json['from_date']
   to_date = request.json['to_date']
   json_input = []
   fin_dict = {}
   sql = json.loads(dbget("SELECT \
        COUNT(CASE WHEN res_guest_status LIKE 'checkin' THEN 1 END) AS Checkin,\
        COUNT(CASE WHEN res_guest_status LIKE 'reserved' THEN 1 END) AS Reserved, \
        COUNT(CASE WHEN res_guest_status LIKE 'waitlist' THEN 1 END) AS Waitlist, \
        COUNT(CASE WHEN res_guest_status LIKE 'Check out' THEN 1 END) AS CheckOut \
        FROM reservation.res_reservation where  res_arrival between '"+from_date+"' and '"+to_date+"'"))
   print(sql)
   psql = sql[0]
   print(psql)
   for k,v in psql.items():
     json_input.append({'title':k,'value':v})
   print(json_input)
        
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))
def GetReservationNoshowreport(request):
   
   from_date = request.json['from_date']
   to_date = request.json['to_date']
   json_input = []
   fin_dict = {}
   sql = json.loads(dbget("SELECT \
	COUNT(CASE WHEN res_guest_status LIKE 'no show' THEN 1 END) AS NoShow, \
	COUNT(CASE WHEN res_guest_status LIKE 'cancel' THEN 1 END) AS Cancel, \
	COUNT(CASE WHEN res_guest_status LIKE 'due in' THEN 1 END) AS DueIn, \
	COUNT(CASE WHEN res_guest_status LIKE 'due out' THEN 1 END) AS DueOut \
        FROM reservation.res_reservation where  res_arrival between '"+from_date+"' and '"+to_date+"'"))
   print(sql)
   psql = sql[0]
   print(psql)
   for k,v in psql.items():
     json_input.append({'title':k,'value':v})
   print(json_input)
        
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))
 

       
def GetFrontDeskReport(request):
   from_date = request.json['from_date']
   to_date = request.json['to_date']
   json_input = []
   fin_dict = {}
   sql = json.loads(dbget("SELECT 'checkin' AS table_name, COUNT(*) FROM reservation.res_reservation where res_guest_status='checkin' and  res_arrival between '"+from_date+"' and '"+to_date+"' \
                            UNION \
                            SELECT 'queue' AS table_name, COUNT(*) FROM room_management.rm_queue_room \
                            UNION \
                            SELECT 'checkout' AS table_name, COUNT(*) FROM reservation.res_reservation where res_guest_status='Check out' and  res_arrival between '"+from_date+"' and '"+to_date+"'"))



   print(sql)
  
   for v in sql:
     json_input.append({'title':v['table_name'],'value':v['count']})
   print(json_input)
        
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))

def GetBusinessBlock(request):
   from_date = request.json['from_date']
   to_date = request.json['to_date']
   json_input = []
   fin_dict = {}

   sql = json.loads(dbget("SELECT \
        COUNT(CASE WHEN status LIKE 'Inquiry' THEN 1 END) AS Inquiry, \
        COUNT(CASE WHEN status LIKE 'Definite' THEN 1 END) AS Definite, \
        COUNT(CASE WHEN status LIKE 'Proposal' THEN 1 END) AS Proposal, \
        COUNT(CASE WHEN status LIKE 'Tentative' THEN 1 END) AS Tentative, \
	COUNT(CASE WHEN status LIKE 'Cancelled' THEN 1 END) AS Cancelled \
        FROM business_block.business_block_definite \
        join business_block.block_status on block_status.id = business_block_definite.block_status_id where start_date between '"+from_date+"' and '"+to_date+"'"))
   print(sql)
   psql = sql[0]
   print(psql)
   for k,v in psql.items():
     json_input.append({'title':k,'value':v})
   print(json_input)
        
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))
       
def GetProfileReport(request):
   from_dates = request.json['from_date']
   to_dates = request.json['to_date']
   print(from_dates,to_dates)
   sql = json.loads(dbget("select pf_individual_profile.pf_type,pf_company_profile.pf_type as pf_type,res_reservation.res_number_of_rooms from reservation.res_reservation \
                            left join profile.pf_individual_profile on pf_individual_profile.pf_id = res_reservation.pf_id \
                            left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.pf_id \
                            where res_arrival between '"+str(from_dates)+"' and '"+str(to_dates)+"'" ))

   room_name = []
   new_ivr_room = []
   res = []
   for room in sql:
            if room['pf_type']  in room_name:
                i = room_name.index(room['pf_type'])
            else:
                room_name.append(room['pf_type'])
                print("name",room_name)
                new_ivr_room.append([])
                i = room_name.index(room['pf_type'])
                
            new_ivr_room[i].append(room)
   print("newivr room",new_ivr_room)
   for rooms in new_ivr_room:

            res.append({"title":rooms[0]['pf_type'],
                       "value":sum(room['res_number_of_rooms'] for room in rooms)})
   print(res)
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":res},indent=2))

def GetRoomHousekeeping(request):
   json_input = []
   fin_dict = {}
   sql = json.loads(dbget("select rm_room ,rm_room_status from room_management.rm_room_list"))
   print(sql)
   for v in sql:
     json_input.append({'title':v['rm_room'],'value':v['rm_room_status']})
   print(json_input)
        
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))
       
def GetFrontofficestatus(request):
   json_input = []
   sql = json.loads(dbget("select rm_room ,rm_fo_status from room_management.rm_room_list"))
   print(sql)
   for v in sql:
     json_input.append({'title':v['rm_room'],'value':v['rm_fo_status']})
   print(json_input)
        
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))
       
def GetRoomconditionall(request):
   print(request.json)
   from_dates = request.json['from_date']
   to_dates = request.json['to_date']
   print(from_dates,to_dates)
   json_input = []
   sql = json.loads(dbget("select res_reservation.res_arrival,rm_room_condition.rm_condition,res_reservation.res_room from reservation.res_reservation \
                           left join room_management.rm_room_condition on rm_room_condition.rm_room = res_reservation.res_room \
                           where res_arrival between '"+str(from_dates)+"' and '"+str(to_dates)+"'"))
   print(sql)
   for v in sql:
      if v['rm_condition'] is None:
         status = "No room condition"
      else:
         status = v['rm_condition']
      json_input.append({'title':v['res_room'],'value':status,'date':v['res_arrival']})
   print(json_input)
        
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))
def GetRoomDiscrepencies(request):
   json_input = []
   from_dates = request.json['from_date']
   to_dates = request.json['to_date']
   print(from_dates,to_dates)
   current_date = datetime.datetime.utcnow()
   current_date = current_date.date()
   sql = json.loads(dbget("select res_reservation.res_arrival,rm_room_discrepancy.rm_room_discrepancy,res_reservation.res_room from reservation.res_reservation \
                           left join room_management.rm_room_discrepancy on rm_room_discrepancy.rm_room = res_reservation.res_room \
                           where res_arrival between '"+str(from_dates)+"' and '"+str(to_dates)+"'"))
   print(sql)
   for v in sql:
    if v['rm_room_discrepancy'] is None:
         status = "No discrepancy"
    else:
         status = v['rm_room_discrepancy']
    json_input.append({'title':v['res_room'],'value':status,'date':v['res_arrival']})
   print(json_input)
        
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))

def GetGuestServiceStatus(request):
   json_input = []
   from_dates = request.json['from_date']
   to_dates = request.json['to_date']
   print(from_dates,to_dates)
   current_date = datetime.datetime.utcnow()
   current_date = current_date.date()
   sql = json.loads(dbget("select res_reservation.res_arrival,guest_service_status.rm_service_status,res_reservation.res_room from reservation.res_reservation \
                           left join room_management.guest_service_status on guest_service_status.rm_room = res_reservation.res_room \
                           where res_arrival between '"+str(from_dates)+"' and '"+str(to_dates)+"'"))
   print(sql)
   for v in sql:
      if v['rm_service_status'] is None:
         status = "No service status"
      else:
         status = v['rm_service_status']
      json_input.append({'title':v['res_room'],'value':status,'date':v['res_arrival']})
   print(json_input)
        
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))

def GetZerobalanceaccount(request):
    
   from_dates = request.json['from_date']
   to_dates = request.json['to_date']

   sql = json.loads(dbget("select count(*) from reservation.res_reservation \
                           where res_guest_balance = 0 and res_arrival between '"+str(from_dates)+"' and '"+str(to_dates)+"'"))

   psql = json.loads(dbget("select count(*) from reservation.res_reservation \
                           where res_guest_balance not in (0) and res_arrival between '"+str(from_dates)+"' and '"+str(to_dates)+"'"))
   json_input = [
      {'title':'Zero balance','value':sql[0]['count']},
      {'title':'Payable Amount','value':psql[0]['count']}   
     ]
   return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))
def futurebooking():
    current_date = datetime.datetime.utcnow()
    current_date = current_date.date()
    #current_date = str(current_date)
    print(current_date)
    dividendlist, dividendlist_add, count_of_year,fin_list = [],[],{},[]
    
    
    Year1 = json.loads(dbget("select res_arrival from reservation.res_reservation  where  res_arrival > '"+str(current_date)+"' and res_guest_status in ('reserved','due in','arrival') order by res_arrival"))
    
    

    print(Year1)
    for dividend_dict in Year1:
     for key, value in dividend_dict.items():
        dividendlist.append(value)
        
    year_count = 0
    for i in dividendlist:
        year_count = year_count+1
        j = datetime.datetime.strptime(i,'%Y-%m-%d').date()
        month_j = j
        sample = "'{}'".format(month_j)
        if sample in dividendlist_add:
            pass
        else: 
           dividendlist_add.append(sample)
           year_count = 1
        count_of_year[""+str(month_j)+""] = year_count

        
    print(count_of_year)
    for k,v in count_of_year.items():
        fin_list.append({'date':k,'value':v})
        #fin_list.append(fin_res['value'] = v)
    print(fin_list)
        
    return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":fin_list},indent=2))

def HistoryBooking():
    current_date = datetime.datetime.utcnow()
    current_date = current_date.date()
    #current_date = str(current_date)
    print(current_date)
    dividendlist, dividendlist_add, count_of_year,fin_list = [],[],{},[]
    
    roomtype = {}
    Year1 = json.loads(dbget("select res_arrival from reservation.res_reservation  where  res_arrival < '"+str(current_date)+"' and res_guest_status ='Check out' order by res_arrival"))
    
   
    print(Year1)
    for dividend_dict in Year1:
     for key, value in dividend_dict.items():
        dividendlist.append(value)
        
    year_count = 0
    for i in dividendlist:
        year_count = year_count+1
        j = datetime.datetime.strptime(i,'%Y-%m-%d').date()
        month_j = j
        sample = "'{}'".format(month_j)
        if sample in dividendlist_add:
            pass
        else: 
           dividendlist_add.append(sample)
           year_count = 1
        count_of_year[""+str(month_j)+""] = year_count

        
    print(count_of_year)
    
    for k,v in count_of_year.items():
        fin_list.append({'date':k,'value':v})
        #fin_list.append(fin_res['value'] = v)
    print(fin_list)
        
    return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":fin_list},indent=2))

def Cashiergettotalamount(request):
        from_date = request.json['from_date']
        to_date = request.json['to_date']

        dividendlist, dividendlist_add, count_of_year,fin_list = [],[],{},[]
    
        roomtype = {}
        ivr_room = json.loads(dbget("select res_arrival,posting_payment.postig_amount from reservation.res_reservation \
                              left join cashiering.posting_payment on posting_payment.res_id = res_reservation.res_id \
                             where  res_reservation.res_arrival between '"+from_date+"' and '"+to_date+"'order by res_arrival"))
    
    
        print(ivr_room)

       
        room_name = []
        new_ivr_room = []
        res = []
        for room in ivr_room:
            if room['res_arrival']  in room_name:
                i = room_name.index(room['res_arrival'])
            else:
                room_name.append(room['res_arrival'])
                print("name",room_name)
                new_ivr_room.append([])
                i = room_name.index(room['res_arrival'])
                
                
            new_ivr_room[i].append(room)
        print("newivr room",new_ivr_room)
        for rooms in new_ivr_room:

            res.append({"title":rooms[0]['res_arrival'],
                       "value":sum(room['postig_amount'] for room in rooms)})
            print(res)
                       
        #print(new_ivr_room)
        print(res)
        #print(room_name)
        return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":res},indent=2))
  
def RoomHistory(request):
    today = datetime.datetime.utcnow().date()
    print(today)
    sql_value = json.loads(dbget("select * from reservation.res_reservation where res_arrival < '"+str(today)+"' order by res_arrival"))
    #print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))


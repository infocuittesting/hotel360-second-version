from sqlwrapper import gensql, dbget,dbput
import json
import datetime
from collections import Counter
def get_rate(s):
   if s == 4:
       return('four_adult_rate')
   elif s == 3:
       return('three_adult_rate')
   elif s == 2:
       return('two_adult_rate')
   elif s == 1:
       return('one_adult_rate')
def HOTEL_REM_POST_SELECT_SelectRateForReservation(r_date, r_code, r_room, r_adult):
   print("inputs: ", r_date, r_code, r_room, r_adult)

   rate1 = json.loads(dbget("SELECT rates_all.rates_id, revenue_management.ratecode.*, \
                             rates_all.rate_details_id, season_code.*, rates_all.rate_date, \
                             rates_all.one_adult_rate, rates_all.two_adult_rate, rates_all.three_adult_rate,\
                             rates_all.four_adult_rate, rates_all.one_child_rate,rates_all.two_child_rate,\
                             rates_all.extra_child_rate, rates_all.rooms_id, rates_all.packages_id,\
                             rate_tier.* from revenue_management.rates_all join \
                             revenue_management.season_code on \
                             rates_all.season_code_id = season_code.season_code_id join \
                             revenue_management.rate_tier on \
                             rates_all.rate_tier_id = rate_tier.rate_tier_id join \
                  revenue_management.ratecode on rates_all.ratecode_id = ratecode.ratecode_id \
                             where rate_date='"+r_date+"' and rate_code='"+r_code+"' "))
                             #where rate_date='"+r_date+"' "))
   print("rate1", rate1, len(rate1))
   if len(rate1) == 1:
       print("rate1[0][get_rate(r_adult)]", rate1[0][get_rate(r_adult)])
       return(rate1[0][get_rate(r_adult)])

   rooms = [rate['rooms_id'] for rate in rate1]
   print(rooms)
   r_id = ''
   for room in rooms:
       if len(r_id) == 0:
           r_id+= "'"+str(room)+"'"
       else:
           r_id+= ","+"'"+str(room)+"'"

   print(r_id)
   rate2 = json.loads(dbget("select rooms_selected.*,room_type.type from revenue_management.rooms_selected \
                             join room_management.room_type\
                          on rooms_selected.room_type_id = room_type.id \
                          where rooms_id in ("+r_id+")"))

   print("rate2",rate2)

   for rates in rate2:

       if rates['type'] == r_room:
           print("type", rates['type'])
           ro_id = rates['rooms_id']
           break

   r_rate = [r[get_rate(r_adult)]  for r in rate1 if r['rooms_id']== ro_id]
   print("r_rate", r_rate[0])
   return(r_rate[0])
def Hotel_END_OF_Day_POST_countrycheck(request):
   today_date = datetime.datetime.utcnow().date()
   print(today_date)
   #country1 = json.loads(dbget("select pf_company_profile.pf_company_country  ,res_reservation.* from reservation.res_reservation \
    #                      left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.pf_id \
     #                     where res_arrival='"+str(today_date)+"'"))
   coutry2 = json.loads(dbget("select pf_individual_profile.pf_individual_country  ,res_reservation.* from reservation.res_reservation \
                          left join profile.pf_individual_profile on pf_individual_profile.pf_id = res_reservation.pf_id \
                          where res_arrival <='"+str(today_date)+"' and res_depature >='"+str(today_date)+"' "))


  # country1  = country1 + coutry2
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':coutry2,'ReturnCode':'RRTS'},indent=2))

def Hotel_END_OF_Day_POST_Departure_Not_Checkedout(request):

   date = json.loads(dbget("select roll_business_date from endofday.business_date"))
   print(date)
   date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
   result = json.loads(dbget("select * from reservation.res_reservation \
                            where res_guest_status = 'due out' and res_depature = '"+str(date)+"' "))

   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result,'ReturnCode':'RRTS'},indent=4))

def Hotel_END_OF_Day_POST_Roll_Business_date(request):
   date = json.loads(dbget("select roll_business_date from endofday.business_date"))
   print(date)
   tomorrow_date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
   dbput("update endofday.business_date set roll_business_date = '"+str(tomorrow_date)+"'")
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','Date':str(tomorrow_date),'ReturnValue':'Record Updated Successfully','ReturnCode':'RUS'},indent=4))

def Hotel_END_OF_Day_POST_Posting_Rooms_charges(request):
   print("Hello world")
   run_charges,d,fixed_rate_id = [],{},[]
   date = json.loads(dbget("select roll_business_date from endofday.business_date"))
   print(date)
   #****************************************Posting fixed rate****************************************************
   sql_value = json.loads(dbget("select res_arrival,res_depature,res_rate,res_id,fixed_rate,	(select count(*) from reservation.res_fixed_rate where res_arrival <= '"+str(date[0]['roll_business_date'])+"' and res_depature >='"+str(date[0]['roll_business_date'])+"') from reservation.res_fixed_rate \
                                 where res_arrival <= '"+str(date[0]['roll_business_date'])+"' and res_depature >='"+str(date[0]['roll_business_date'])+"'"))
   print(sql_value)
   if len(sql_value) >0:
      for i in sql_value:
         fixed_rate_id.append(i['res_id'])
         psql = json.loads(dbget("select res_room,pf_firstname from reservation.res_reservation \
                                  where res_id = '"+str(i['res_id'])+"'"))
         d['res_room'] = psql[0]['res_room']
         d['res_id'] = i['res_id']
         d['posting_amount'] = i['res_rate']
         d['posting_date'] = date[0]['roll_business_date']
         d['post_code_id'] = '5020'
         d['post_window'] = '1'
         d['posting_supplement'] = 'Fixed rate Posting'
         d['posting_reference'] = 'Fixed rate Posting room chrages'
         d['posting_quantity'] = '1'
         d['emp_id'] = 1
         gensql('insert','cashiering.billing_post',d)
         run_charges.append({'room':psql[0]['res_room'],
                             'name':psql[0]['pf_firstname'],
                             'posting':'posting room and tax'})
      print(fixed_rate_id)
   else:
      print("posting room charges")
      if len(fixed_rate_id) > 0:
   #****************************************Posting Rooms and tax charges **************************************************
         sql_value = json.loads(dbget("select * from reservation.res_reservation \
                                       where res_arrival <= '"+str(date[0]['roll_business_date'])+"' and res_depature >='"+str(date[0]['roll_business_date'])+"' \
                                       res_id not in ("+set(fixed_rate_id)+")"))
      else:
         sql_value = json.loads(dbget("select * from reservation.res_reservation \
                                       where res_arrival <= '"+str(date[0]['roll_business_date'])+"' and res_depature >='"+str(date[0]['roll_business_date'])+"' "))
      for i in sql_value:
         data = HOTEL_REM_POST_SELECT_SelectRateForReservation(date[0]['roll_business_date'],i['res_rate_code'],i['res_room_type'],i['res_adults'])
         d['res_room'] = i['res_room']
         d['res_id'] = i['res_id']
         d['posting_amount'] = data
         d['posting_date'] = date[0]['roll_business_date']
         d['post_code_id'] = '5020'
         d['post_window'] = '1'
         d['posting_supplement'] = 'Room charges Posting'
         d['posting_reference'] = 'posting room chrages'
         d['posting_quantity'] = '1'
         d['emp_id'] = 1
         gensql('insert','cashiering.billing_post',d)
         run_charges.append({'room':i['res_room'],
                             'name':i['pf_firstname'],
                             'posting':'posting room and tax'})
   #****************************************Fixed Charges ********************************************************************

   fixed_charge = json.loads(dbget("select res_reservation.res_room, \
	                           res_fixed_charges.res_id, fixed_charges_occurrence, fixed_charges_begin_date, \
                                   fixed_charges_end_date, fixed_charges_transaction_code, fixed_charges_article_code, fixed_charges_amount, \
                                   fixed_charges_quantity, fixed_charges_supplement, fixed_charges_id, res_fixed_charges.res_unique_id \
	                           FROM reservation.res_fixed_charges \
                                   left join reservation.res_reservation on res_reservation.res_unique_id = res_fixed_charges.res_unique_id \
	                           where fixed_charges_begin_date <= '"+str(date[0]['roll_business_date'])+"' and fixed_charges_end_date >='"+str(date[0]['roll_business_date'])+"'"))


   for fix_cha in fixed_charge:
      fixed_charge_code = json.loads(dbget("select posting_code from cashiering.billing_code \
                                            where posting_code_description = '"+fix_cha['fixed_charges_transaction_code']+"'"))
      d['res_room'] = fix_cha['res_room']
      d['res_id'] = fix_cha['res_id']
      d['posting_amount'] = fix_cha['fixed_charges_amount'] * fix_cha['fixed_charges_quantity']
      d['posting_date'] = date[0]['roll_business_date']
      d['post_code_id'] = fixed_charge_code[0]['posting_code']
      d['post_window'] = '1'
      d['posting_supplement'] = 'Night Audit Posting'
      d['posting_reference'] = 'Night Audit Posting posting fixed chrages'
      d['posting_quantity'] = fix_cha['fixed_charges_quantity']
      d['emp_id'] = 1
      gensql('insert','cashiering.billing_post',d)

      #run_charges = [ x['fixed_charges']='fixed charges run' for x in run_charges if x['room'] == fix_cha['res_room'] ]
      for x in run_charges:
          if x['room'] == fix_cha['res_room']:
             i = run_charges.index(x)
             print("i", i)
             run_charges[i]['fixed_charges'] = 'fixed charges run'

   #***********************************************Posting Packages***********************************************************
   print("packages is pending")

   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':run_charges,'ReturnCode':'RRTS'},indent=4))
def Hotel_END_OF_Day_POST_Run_Additional_procedures(request):
    run_additional,list1,list2,no_show_count,list3,list4,dic_pancy,d = [],[],[],[],[],[],[],{}
    #********************* night audit date******************

    date = json.loads(dbget("select roll_business_date from endofday.business_date"))
    print(date)

    no_show_date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) - datetime.timedelta(days=1)
    #******************** Reservation No show***********************
    no_show = json.loads(dbget("select res_id,res_unique_id,res_guest_status from reservation.res_reservation \
                               where res_arrival='"+str(no_show_date)+"' \
                               and res_guest_status = 'arrival'"))
    #print(no_show)

    no_show_start_time = datetime.datetime.now()
    for no_show_report in no_show:
        no_show_count.append(no_show_report['res_guest_status'])
        no_show_update = dbput("update reservation.res_reservation set res_guest_status = 'no show' \
                               where res_id = '"+str(no_show_report['res_id'])+"' \
                               and res_unique_id = '"+str(no_show_report['res_unique_id'])+"'")

        #print(no_show_update)
    no_show_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Reservation No Show","start_time":str(no_show_start_time.strftime("%H:%M:%S")),"end_time":str(no_show_end_time.strftime("%H:%M:%S")),"Iteration": len(no_show_count),"Status":"Completed"})
    #*********************************Due in ************************************************
    due_in_date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
    due_in = json.loads(dbget("select res_id,res_unique_id,res_guest_status from reservation.res_reservation \
                               where res_arrival='"+str(due_in_date)+"'"))
    due_in_start_time = datetime.datetime.now()
    for due_in_report in due_in:
        list1.append(due_in_report['res_unique_id'])
        due_in_update = dbput("update reservation.res_reservation set res_guest_status = 'due in' \
                               where res_id = '"+str(due_in_report['res_id'])+"' \
                               and res_unique_id = '"+str(due_in_report['res_unique_id'])+"' \
                               and res_guest_status not in ('cancel')")
    due_in_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Reservation Due In",
                           "start_time":str(due_in_start_time.strftime("%H:%M:%S")),"end_time":str(due_in_end_time.strftime("%H:%M:%S")),"Iteration": len(list1),"Status":"Completed"})

    #************************************************* Due Out****************************************
    due_out_date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
    due_out = json.loads(dbget("select res_id,res_unique_id,res_guest_status from reservation.res_reservation \
                               where res_depature='"+str(due_out_date)+"'"))
    due_out_start_time = datetime.datetime.now()
    for due_out_report in due_out:
        list2.append(due_out_report['res_unique_id'])
        due_out_update = dbput("update reservation.res_reservation set res_guest_status = 'due out' \
                               where res_id = '"+str(due_out_report['res_id'])+"' \
                               and res_unique_id = '"+str(due_out_report['res_unique_id'])+"' \
                               and res_guest_status not in ('cancel,no show')")
    print(list2)
    due_out_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Reservation Due Out",
                           "start_time":str(due_out_start_time.strftime("%H:%M:%S")),"end_time":due_out_end_time.strftime("%H:%M:%S"),"Iteration": len(list2),"Status":"Completed"})

    #*******************************arrival ****************************************************************
    #arrival_date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
    arrivals = json.loads(dbget("select res_id,res_unique_id,res_guest_status from reservation.res_reservation \
                               where res_arrival='"+str(date[0]['roll_business_date'])+"'"))
    arrival_start_time = datetime.datetime.now()
    for arrivals_report in arrivals:
        list3.append(arrivals_report['res_unique_id'])
        arrivals_report_update = dbput("update reservation.res_reservation set res_guest_status = 'arrival' \
                               where res_id = '"+str(arrivals_report['res_id'])+"' \
                               and res_unique_id = '"+str(arrivals_report['res_unique_id'])+"' \
                               and res_guest_status not in ('cancel,no show') ")
    #print(list3)
    arrival_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Reservation Arrival",
                           "start_time":str(arrival_start_time.strftime("%H:%M:%S")),"end_time":str(arrival_end_time.strftime("%H:%M:%S")),"Iteration": len(list3),"Status":"Completed"})


    #**********************************In-house guest**********************************************
    in_house =  json.loads(dbget(" select * from reservation.res_reservation where res_guest_status='checkin' or res_guest_status='due out'"))
    in_house_start_time = datetime.datetime.now()
    for in_house_report in in_house:
        list4.append(in_house_report['res_unique_id'])
    in_house_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"In-House Guest",
                           "start_time":str(in_house_start_time.strftime("%H:%M:%S")),"end_time":str(in_house_end_time.strftime("%H:%M:%S")),"Iteration": len(list4),"Status":"Completed"})

    #***************************************Room Discrepancy********************************
    room_discrepancy = json.loads(dbget("select * from room_management.rm_room_list \
                                        where rm_fo_status = 'occupied' and rm_hk_status = 'vacant'"))
    room_disc_start_time = datetime.datetime.now()
    for discrepancy in room_discrepancy:
       dic_pancy.append(discrepancy['rm_room'])
       d['rm_room'] = discrepancy['rm_room']
       d['rm_room_discrepancy'] = 'Skip'
       skip_person = gensql('insert','room_management.rm_room_discrepancy',d)
    sleep_details = json.loads(dbget("select * from room_management.rm_room_list \
                                    where rm_fo_status = 'vacant' and rm_hk_status = 'occupied'"))
    for sleep in sleep_details:
       dic_pancy.append(discrepancy['rm_room'])
       d['rm_room'] = sleep['rm_room']
       d['rm_room_discrepancy'] = 'Sleep'
       sleep_person = gensql('insert','room_management.rm_room_discrepancy',d)
    person_details = json.loads(dbget("select * from room_management.rm_room_list"))
    preson_differ = list(filter(lambda x:x['rm_hk_person']!=x['rm_fo_person'],person_details))
    for preson in preson_differ:
          d['rm_room'] = preson['rm_room']
          d['rm_room_discrepancy'] = 'Person'
          person_differ_details = gensql('insert','room_management.rm_room_discrepancy',d)
    room_disc_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Room Discrepancies",
                           "start_time":str(room_disc_start_time.strftime("%H:%M:%S")),"end_time":str(room_disc_end_time.strftime("%H:%M:%S")),"Iteration": len(dic_pancy),"Status":"Completed"})
    def serialize(obj):
        if isinstance(obj, datetime.date):
       
               return obj.__str__()

        if isinstance(obj, datetime.time):
               return obj.__str__()
    return (json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':run_additional,'ReturnCode':'RRTS'},indent=4,default=serialize))
def Hotel_END_OF_Day_POST_print_final_report(request):
    #*******************************room cleaning report*******************
    list1,list2 = [],[]
    date = json.loads(dbget("select roll_business_date from endofday.business_date"))
    print(date)
    sql_value = json.loads(dbget("select * from reservation.res_reservation \
	where res_guest_status in('due out','checkin','Checkout') and res_arrival <='"+str(date[0]['roll_business_date'])+"' and res_depature >= '"+str(date[0]['roll_business_date'])+"'"))

    for i in sql_value:
        rooms = json.loads(dbget("select * from room_management.rm_room_list \
                              where rm_room = '"+str(i['res_room'])+"'"))
        list1.append({
        "room":i['res_room'],
        "room_type":rooms[0]['rm_room_type'],
        "room_class":rooms[0]['rm_room_class'],
        "room_status":"Dirty"

        })
    list2.append({"Report_Name":"RoomCleaningReport","reportstatus":"filed","room_repport_file":list1})
    #*******************************in-house report**************************
    in_house =  json.loads(dbget(" select * from reservation.res_reservation where\
	res_guest_status='checkin' or res_guest_status='due out' and res_arrival <='"+str(date[0]['roll_business_date'])+"' and res_depature >='"+str(date[0]['roll_business_date'])+"'"))
    list2.append({"Report_Name":"IN-houseReport","reportstatus":"filed","room_repport_file":in_house})
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':list2,'ReturnCode':'RRTS'},indent=4))

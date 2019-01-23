from sqlwrapper import gensql, dbget,dbput
import json
import datetime

date = json.loads(dbget("select roll_business_date from endofday.business_date"))
print(date)
next_day = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
yesterday_date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) - datetime.timedelta(days=1)

    
#todays_date = datetime.datetime.utcnow().date()
def Hotel_PMS_Select_GetTodayRoomAvailabilityArrival(request):
    
    final = []
   
    sql = json.loads(dbget("SELECT 'checkin' as dash_board ,COUNT(*) FROM reservation.res_reservation WHERE res_guest_status='checkin' and res_arrival='"+str(date[0]['roll_business_date'])+"' \
                            union \
                            SELECT 'checkout' , COUNT(*) FROM reservation.res_reservation WHERE res_guest_status='Check out' and res_depature='"+str(date[0]['roll_business_date'])+"' \
                            union \
                            SELECT 'arrival' ,COUNT(*) FROM reservation.res_reservation WHERE res_guest_status ='arrival' and res_arrival='"+str(date[0]['roll_business_date'])+"' \
                            union \
                            select 'due_out' , count(*) from reservation.res_reservation where res_guest_status='due out' and  res_depature ='"+str(next_day)+"' \
                            union \
                            select 'reservation' ,count(*) from reservation.res_reservation where created_on='"+str(date[0]['roll_business_date'])+"' \
                            union  \
                            select 'room_availability' ,count(*) from room_management.rm_room_list where rm_reservation_status='not reserved'  "))
    print(sql)
   
   
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'ReturnCode':'RRTS'},indent=4))

def Hotel_PMS_cancel_DepositRuleReservation(request):
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    sql = json.loads(dbget("select res_id from reservation.res_deposit \
                            where res_due_date = '"+str(yesterday_date)+"'"))
    
    for i in sql:
        
        psql = dbput("update reservation.res_reservation set res_guest_status = 'cancel' \
                     where res_id = '"+str(i['res_id'])+"'")
        print(psql)
        select = json.loads(dbget("select * from reservation.cancel_id"))
        print(select,type(select),len(select))
        print(select[0]['id'])
        cancel_id = str(select[0]['id']+1)
        print(cancel_id)
        update = dbput("update reservation.cancel_id set id = '"+str(select[0]['id']+1)+"'")
        s = {}
        s['Emp_Id'] = '121'
        s['Emp_Firstname'] = 'Ranimangama'
       
        s['RES_Log_Date'] = datetime.datetime.utcnow().date()
        s['RES_Log_Time'] = RES_Log_Time
        s['RES_Action_Type'] = "Cancel Reservation"
        s['RES_Description'] = "cancellation Number is" +" "+ cancel_id
        s['Res_id'] = i['res_id']
        
        sql_value = gensql('insert','reservation.res_activity_log',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
    
def Hotel_PMS_Select_BlockFollowupDecisiondate(request):
    datelist = []
    d = request.json
    sql =json.loads(dbget("select follow_date,decision_date FROM business_block.block_room where block_id = '"+str(d['block_id'])+"'"))
    #print(sql)
    date1 = datetime.datetime.strptime(sql[0]['follow_date'], '%Y-%m-%d').date()
    date2 = datetime.datetime.strptime(sql[0]['decision_date'], '%Y-%m-%d').date()
    businessdate = datetime.datetime.strptime(date[0]['roll_business_date'], '%Y-%m-%d').date()
    #print(date1,date2,type(date1))
    delta = date2 - date1         # timedelta

    for i in range(delta.days + 1):
        #print(i)
        #print(date1 + datetime.timedelta(i))
        datelist.append(str(date1 + datetime.timedelta(i)))
        #date1 = date1 + datetime.timedelta(days=7)
    print(datelist)
    for i in datelist:
        dateform = datetime.datetime.strptime(i, '%Y-%m-%d').date()
        print(dateform)
        if dateform == businessdate:
    
            return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Valid','ReturnCode':'RV'}, sort_keys=True, indent=4))
            
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record InValid','ReturnCode':'RIV'}, sort_keys=True, indent=4))

def Hotel_PMS_Select_Blockcutoffdatecutoffdays(request):
    
    datelist = []
    d = request.json
    businessdate = datetime.datetime.strptime(date[0]['roll_business_date'], '%Y-%m-%d').date()
    sql =json.loads(dbget("   select block_room.cutoff_days,block_room.cutoff_date,business_block_definite.block_created_date \
                           from business_block.business_block_definite, business_block.block_room \
                           where business_block_definite.block_id = '"+str(d['block_id'])+"' and block_room.block_id='"+str(d['block_id'])+"'"))
    print(sql)
    initial=datetime.datetime.strptime(sql[0]['block_created_date'], '%Y-%m-%d').date()
    date1 = initial + datetime.timedelta(days=1)
    date2 = date1 + datetime.timedelta(days=sql[0]['cutoff_days'])
    delta = date2-date1
    if sql[0]['cutoff_date'] is not None:
        dateform = datetime.datetime.strptime(sql[0]['cutoff_date'], '%Y-%m-%d').date()
        print(sql[0]['cutoff_date'])
        if dateform == businessdate:
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Valid','ReturnCode':'RV'}, sort_keys=True, indent=4))
            
    else:
        pass
    
    if sql[0]['cutoff_days'] is not None:
      
        for i in range(delta.days + 1):
        #print(i)
            print(date1 + datetime.timedelta(i))
        
            if date1 + datetime.timedelta(i) == businessdate:
                return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Valid','ReturnCode':'RV'}, sort_keys=True, indent=4))
        
           
    else:
        pass
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record InValid','ReturnCode':'RIV'}, sort_keys=True, indent=4))


def Hotel_PMS_Select_DepositDueDate(request):
    d = request.json
    sql = json.loads(dbget("select res_due_date from reservation.res_deposit \
                           where res_id = '"+str(d['res_id'])+"' and res_block is null or res_block = '' "))
    print(sql)
    businessdate = datetime.datetime.strptime(date[0]['roll_business_date'], '%Y-%m-%d').date()
    for i in sql:
        if i['res_due_date'] is not None:
            dateform = datetime.datetime.strptime(i['res_due_date'], '%Y-%m-%d').date()
            print(dateform)
            if dateform == businessdate:
                return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Valid','ReturnCode':'RV'}, sort_keys=True, indent=4))
        else:
             pass
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record InValid','ReturnCode':'RIV'}, sort_keys=True, indent=4))

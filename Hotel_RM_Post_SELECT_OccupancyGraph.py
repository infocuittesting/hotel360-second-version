from sqlwrapper import gensql, dbget
import json
import datetime
from collections import Counter
def Hotel_RM_Post_SELECT_OccupancyGraph(request):


    d = request.json
    e ,list1,list2,final_value,list3= {},[],[],[],[]

    date1 = datetime.datetime.strptime(d['start_date'], '%Y-%m-%d').date()
    date2 = date1 + datetime.timedelta(days=6)
    roomcount = json.loads(dbget("select count(*) from room_management.rm_room_list"))
    print(roomcount[0]['count'])
    sql_value = json.loads(dbget("select res_arrival from reservation.res_reservation \
                                  where res_arrival between '"+str(date1)+"' and   '"+str(date2)+"' "))

    list1 = [{'date':k,'deduct':v,'nondeduct':roomcount[0]['count'] - v,'total_room':roomcount[0]['count']} for k,v in Counter([i['res_arrival'] for i in sql_value]).items()]
    list2 = [{'date':str(datetime.datetime.strptime(k, '%Y-%m-%d').date().strftime("%b %d")),'deduct':v,'nondeduct':roomcount[0]['count'] - v,'total_room':roomcount[0]['count']} for k,v in Counter([i['res_arrival'] for i in sql_value]).items()]
    #print(list1)
    list1_date = [i['date'] for i in list1]
    
    while  date1 <= date2:
        if str(date1) not in list1_date:
          # date1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
           list2.append({'date':str(date1.strftime("%b %d")),'deduct':0,'nondeduct':roomcount[0]['count'],'total_rooms':roomcount[0]['count']})
        date1 = date1 + datetime.timedelta(days=1)

    final_value = sorted(list2,key = lambda x: x['date'] )

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':final_value  ,'ReturnCode':'RRTS'},indent=4))


def Hotel_RM_Post_SELECT_FacilityForecast(request):

   d = request.json

   list1 ,faclity,list2,arrival = [],{},[],[]
   date1 = datetime.datetime.strptime(d['start_date'], '%Y-%m-%d').date()
   date2 = date1 + datetime.timedelta(days=6)

   sql_value = json.loads(dbget("select res_arrival,res_depature,res_adults,res_child,res_number_of_rooms from reservation.res_reservation \
                                     where res_arrival between   '"+str(date1)+"' and '"+str(date2)+"' \
                    and res_depature between   '"+str(date1)+"' and '"+str(date2)+"' \
                    order by res_arrival,res_depature "))
   #print(sql_value)
   arrival_count = 0
   print(Counter([i['res_arrival'] for i in sql_value]))
   def arrival_and_dep_rooms(date1,name):
       #print('name',name)
       arrival = [v for k,v in Counter([i[""+name+""] for i in sql_value if i[""+name+""]==str(date1)]).items()]
       return (arrival[0] if len(arrival)!=0 else 0)

   def inhouse(date1,name):
       inhouse_count = sum([ i[""+name+""]
                           for i in sql_value
                           if datetime.datetime.strptime(i['res_arrival'], '%Y-%m-%d').date()== date1])

       #or date1 in datetime.datetime.strptime(i['res_depature'], '%Y-%m-%d').date()])

       return(inhouse_count)

   while  date1 <= date2:
        list2.append({'days':date1.strftime("%A"),'date':str(date1),'values':{'arrival_rooms':arrival_and_dep_rooms(date1,name='res_arrival'),
                                                  'depature_rooms':arrival_and_dep_rooms(date1,name='res_depature'),
                                                  'adult_inhouse':inhouse(date1,name='res_adults'),
                                                  'child_inhouse':inhouse(date1,name='res_child')}})
        date1 = date1 + datetime.timedelta(days=1)
   #print(list2)
   '''
   list1 = [{'date':k,'depature_rooms':v} for k,v in Counter([i['res_depature'] for i in sql_value]).items()]
   print(list1)
   list1_date = [i['date'] for i in list1]
   while  date1 <= date2:
       if str(date1) not in list1_date:
          list1.append({'date':str(date1),'depature_rooms':0})
       date1 = date1 + datetime.timedelta(days=1)

   final_value = sorted(list1,key = lambda x: x['date'] )

   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':final_value  ,'ReturnCode':'RRTS'},indent=4))
   '''
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':list2  ,'ReturnCode':'RRTS'},indent=4))

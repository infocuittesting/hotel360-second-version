import json
from sqlwrapper import gensql,dbget,dbput
import datetime

def ratecategory(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.ratecategory',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

def ratecode(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.ratecode',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

def market(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.market',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
def sourcetab(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.source',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
def crrencytab(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.currency',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
def negotiated(request):
    d = request.json
    print(d)
    i = json.loads(dbget("select count(*) from revenue_management.negotiated_rate where rate_code_id="+str(d['rate_code_id'])+""))
    print(i)
    if int(i[0]['count']) == 0 :
       gensql('insert','revenue_management.negotiated_rate',d)
       return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
    else:
       return(json.dumps({"Return": "Record Already Exist","ReturnCode": "RAE","Status": "Success","StatusCode": "200"},indent=4)) 
    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))


def ratedetailss(request):
    
    d = request.json
    print(d)
        
    e = { k : v for k,v in d.items() if k not in ('days','room_types','package','start_date','end_date')}
    print("e",e)

    get_code = { k : v for k,v in d.items() if k in ('ratecode_id','start_date','end_date')}
    print("get_code",get_code)

    gensql('insert','revenue_management.rate_details',get_code)
    rate_details_id = json.loads(gensql('select','revenue_management.rate_details','max(rate_details_id) as number1',get_code))
    print(rate_details_id)
    e['rate_details_id'] = int(rate_details_id[0]['number1'])
    
    room_id = json.loads(dbget("select max(rooms_id) as number1 from revenue_management.rooms_selected"))
    #print("room_id",room_id[0]['number1'])    
    for i in d['room_types']:
        #pass
        dbput("insert into revenue_management.rooms_selected (rooms_id,room_type_id) \
               values ('"+str(room_id[0]['number1']+1)+"','"+str(i)+"') ")
    e['rooms_id'] = int(room_id[0]['number1']+1)
    #print("2222",e)
    if d['rate_tier_id'] == 0:
            
       package_id = json.loads(dbget("select max(packages_id) as number2 from revenue_management.packages_selected"))
       print("package_id",package_id[0]['number2'],type(package_id[0]['number2']))
       for j in d['package']:
         print(j)
         dbput("insert into revenue_management.packages_selected (packages_id,package_code_id) \
               values ('"+str(package_id[0]['number2']+1)+"','"+str(j)+"')")
       e['packages_id'] =  int(package_id[0]['number2']+1)
    print("3333",e)

    days = d['days']
    day1 = [ k  for k,v in days.items() if v != 0 ]
    #print(a,days,day1)
    from_date = request.json['start_date']
    to_date = request.json['end_date']
    from_date = datetime.datetime.strptime(from_date,'%Y-%m-%d').date()
    to_date = datetime.datetime.strptime(to_date,'%Y-%m-%d').date()
    
    while from_date <= to_date:
          print(from_date,from_date.strftime("%A")[0:3].lower())
          if from_date.strftime("%A")[0:3].lower() in day1:
              e['rate_date'] = from_date
              gensql('insert','revenue_management.rates_all',e)
          from_date+=datetime.timedelta(days=1)    
    
    return(json.dumps({"Return": "Record Inserted Successfully",
                       "ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
           

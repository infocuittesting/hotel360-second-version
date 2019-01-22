import datetime
from sqlwrapper import gensql, dbget, dbput
import json
import random

def HOTEL_BBL_POST_INSERT_BusinessBlockDefinite(request):
    d = request.json
    
    x,y,z,p,r,pack,inventory = {},{},{},{},{},{},{}
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    RES_Log_Date = datetime.datetime.utcnow().date()
    #print(RES_Log_Date)
    #<---------------generate block id -------------------------------------->
    sql_value = json.loads(dbget("select count_id from business_block.count"))
    print(sql_value,type(sql_value))
    sql_value1 = sql_value[0]['count_id']
    #sql = int(sql_value1)
    print(sql_value1,type(sql_value1))
    count = sql_value1 + 1
    print(count)
    psql = dbput("update business_block.count set count_id = '"+str(sql_value[0]['count_id']+1)+"'")
    print(psql)
    #<------------------------------------------------------------------------------>
    #<--------------------------generate block name & block code -------------------->
   

   
    x = d['Definite']
    x = { k : v for k,v in x.items() if  v != ''}
    random_no = (random.randint(1000000000,9999999999))
    random_no = str(random_no)
    random_no = random_no[0:4]
    print(random_no)
    pf_id = x.get("pf_id")
    PF_ACCOUNT = json.loads(dbget("select pf_account from profile.pf_company_profile where pf_id = '"+pf_id+"'"))
    PF_ACCOUNT = PF_ACCOUNT[0]['pf_account']
    pf_account = PF_ACCOUNT[0:5]
    x['block_id'] = count
    x['block_code'] = random_no + pf_account
    #x['block_name'] = PF_ACCOUNT
    print("Definite",x,type(x),len(x))
    if len(x) != 0:
       sql1 = gensql('insert','business_block.business_block_definite',x)
       print(sql1)
       s = {}
       blockcode = x.get("block_code")
       blockid = x.get("block_id")
       s['user_role'] = "Supervisor"
       s['date'] = RES_Log_Date
       s['time'] = RES_Log_Time
       s['block_id'] = blockid
       s['action_type_id'] = "New Block Header"
       s['description'] = "Block created successfully"+" "+str(blockid)
       gensql('insert','business_block.business_block_activity_log',s)
      
    else:
       pass
    #<---------------------------rooms tab-------------------------->   
    #y = { k : v for k,v in d.items()if v != ''  if  k  in ('Rooms')}
    y = d['Rooms']
    if y['packages'] != "":
        for val in y['packages']: 
            pack['block_id'] = count
            pack['packages_id'] = val
            gensql('insert','business_block.block_packages',pack)
    else:
        pass
    if y['inventory_control_id'] != "":
        for values in y['inventory_control_id']: 
            inventory['block_id'] = count
            inventory['item_inventory_id'] = values
            gensql('insert','business_block.item_inventory',inventory)
    else:
        pass
    y = { k : v for k,v in y.items() if  v != '' if k not in ('packages','inventory_control_id')}
    
    print("Rooms",y,type(y),len(y))
    if len(y) != 0:
        y['block_id'] = count
        sql2 = gensql('insert','business_block.block_room',y)
        print(sql2)
        
    else:
        pass
    #<------------------------details tab----------------------------->    
    #z = { k : v for k,v in d.items()if v != ''  if  k  in ('Block_details')}
    z = d['Block_details']
    z = { k : v for k,v in z.items() if  v != ''}
   
    print("Block_details",z,type(z),len(z))
    if len(z) != 0:
        z['block_id'] = count
        sql3 = gensql('insert','business_block.block_business_details',z)
        print(sql3)

    else:
        pass
    #<---------------------------------catering----------------------->    
    #p = { k : v for k,v in d.items()if v != ''  if  k  in ('Catering')}
    #print(p)
    p = d['Catering']
    p = { k : v for k,v in p.items() if  v != ''}
    
    print("Catering",p,type(p),len(p))
    if len(p) != 0:
        p['block_id'] = count
        sql4 = gensql('insert','business_block.block_catering',p)
        print(sql4)
        s = {}
        s['user_role'] = "Supervisor"
        blockid = p.get("block_id")

        s['date'] = RES_Log_Date
        s['time'] = RES_Log_Time
        s['block_id'] = blockid
        s['action_type_id'] = "Block Catering"
        s['description'] = "Block Catering for"+" "+str(blockid)
        gensql('insert','business_block.business_block_activity_log',s)
        
    else:
        pass


    #<--------------------------------concurrent meeting tab-------------------------------->
    r = d['block_meeting']
    r = { k : v for k,v in r.items() if  v != ''}
    
    print("block_meeting",r,type(r),len(r))
    if len(r) != 0:
        r['block_id'] = count
        sql5 = gensql('insert','business_block.block_meeting',r)
        print(sql5)
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS','Blockid':blockid,'blockcode':blockcode}, sort_keys=True, indent=4))
   

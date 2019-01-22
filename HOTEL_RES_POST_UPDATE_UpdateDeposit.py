from sqlwrapper import gensql
import json
def HOTEL_RES_POST_UPDATE_UpdateDeposit(request):
    s = {}
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('Res_id','deposit_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('Res_id','deposit_id')}

    print(e)
    sql_value = gensql('update','reservation.res_deposit',a,e)
    query_id = json.loads(dbget("select sum(res_deposit_amount) as deposit_amount,count(*) from reservation.res_deposit where res_id = '"+str(e['Res_id'])+"'"))
    #print(query_id)
    getanother = json.loads(dbget("select count(*)  from reservation.guest_deposit where guest_deposit.res_id = '"+str(e['Res_id'])+"'"))
    #print(getanother)
    if query_id[0]['count'] != 0:
   
        if getanother[0]['count'] !=0:
            sql = dbput("update reservation.guest_deposit set total_amount =  '"+str(query_id[0]['deposit_amount'])+"'\
                        where res_id = '"+e['Res_id']+"'")
            print(sql)
        else:
        
            s['res_id'] = int(e['Res_id'])
            s['total_amount'] = int(query_id[0]['deposit_amount'])
            psql = gensql('insert','reservation.guest_deposit',s)
            print(psql)
    else:
        pass
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

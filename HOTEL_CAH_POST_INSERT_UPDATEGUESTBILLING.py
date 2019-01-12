import json
from sqlwrapper import gensql,dbget,dbput
import datetime

def HOTEL_CAH_POST_INSERT_UPDATEGUESTBILLING(request):
    to_amount = {}
    result = request.json
    #print(result)
    d = result['bills']
    #print(d,type(d))
    res_id = result['Res_id']
    res_room = result['res_room']
    Total_amount = result['Total_amount']
    Total_posting = result['Total_posting']
    print(res_id,res_room,Total_amount,type(res_id),type(res_room),type(Total_amount))
    #print(d,type(d),len(d))
    Posting_date = datetime.datetime.utcnow().date()

    fo_count = json.loads(dbget('select * from cashiering.folio_number'))
    print(fo_count[0]['folio_no'],type(fo_count[0]['folio_no']))
    dbput("update cashiering.folio_number set folio_no = "+str(fo_count[0]['folio_no']+1)+" ")
    folio = {}
    folio['res_id'],folio['total_posting'],folio['total_amount'],folio['folio_no'] = res_id,Total_posting,Total_amount,fo_count[0]['folio_no']+1    
    gensql('insert','cashiering.reservation_folio',folio)
    
    
    for i in range(len(d)):
        total_revenue_count = json.loads(dbget("select count(*) from cashiering.billing_total_revenue \
                                           where res_id = '"+str(res_id)+"'"))
        print(total_revenue_count)
        e = { k : v for k,v in d[i].items() if k not in ('editFlag','Post_des')}
        #print(i)
        #print(d,type(d),len(d))
        e['Posting_date'] = Posting_date
        e['Res_id'] = res_id
        e['res_room'] = res_room
        e['folio_no'] = fo_count[0]['folio_no']+1
        #print(d)
        gensql('insert','cashiering.billing_post',e)
        print(total_revenue_count[0]['count'])
        print(e['Post_window'],type(e['Post_window']))
        if total_revenue_count[0]['count'] != 0:
            if e['Post_window'] == '1'  :
                revenue_count = dbput("update cashiering.billing_total_revenue set total_revenue = total_revenue +'"+str(e['Posting_amount'])+"' \
                                      where res_id = '"+str(res_id)+"' and res_room = '"+str(res_room)+"'")
                print(revenue_count)
            else:
                pass
        else:
            if e['Post_window'] == '1':
                to_amount['res_id'] = res_id
                to_amount['res_room'] = res_room
                to_amount['total_revenue'] = e['Posting_amount']
                revenue_repott = gensql('insert','cashiering.billing_total_revenue',to_amount)
            
                print(revenue_repott)
            else:
                pass
    #dbput("update reservation.res_reservation set res_guest_balance = res_guest_balance + "+str(int(Total_amount))+" \
    #       where res_id='"+res_id+"' and res_room='"+res_room+"' ")
    
    Revenue_date = datetime.datetime.utcnow().date()
    
    result = json.loads(dbget("select log_link_id from cashiering.log_link where link_id='1' "))
    log_id = result[0]['log_link_id']+1
    print(log_id)
    dbput("update cashiering.log_link set log_link_id="+str(log_id)+" where link_id='1'")
    
    s = {}
    s['Posting_date'] = Posting_date
    s['Revenue_date'] = Revenue_date
    s['User_role'] = "Supervisor"
    s['User_name'] = "david"
    s['Res_id'] = res_id
    s['Posting_action'] = "General posting"
    s['Posting_reason'] = "Payment posted for"+ " "+res_id
    s['Posting_description'] = "Payment posted "
    s['log_link_id'] = log_id    
    gensql('insert','cashiering.posting_history_log',s)
    gensql('insert','cashiering.posting_original_history_log',s)
    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

   


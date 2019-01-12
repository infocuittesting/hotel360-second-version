from sqlwrapper import dbget,dbput,gensql
import json

def hotel_rm_post_select_queryoutoforderservice(request):
    sql = json.loads(dbget("select rm_room_list.rm_room_class ,rm_room_mainteanance_acitivity_log.* from \
                            room_management.rm_room_mainteanance_acitivity_log \
                          left join room_management.rm_room_list on rm_room_list.rm_room = rm_room_mainteanance_acitivity_log.rm_room "))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))


def hotel_rm_post_update_updateoutoforderservice(request):
   dict1 = request.json
  
   e = { k : v for k,v in dict1.items() if k in ('rm_room')}
   print(e)
   d = { k : v for k,v in dict1.items() if k not in ('rm_room')}
  
   print(gensql('update','room_management.rm_room_mainteanance_acitivity_log',d,e))
   sql= dbput("update room_management.rm_room_list set rm_room_status = '"+dict1['rm_status']+"' \
                   where rm_room = '"+dict1['rm_room']+"'")
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))




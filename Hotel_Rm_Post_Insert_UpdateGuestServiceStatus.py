from sqlwrapper import gensql,dbget
import json

def hotel_rm_post_insert_updateguestservicestatus(request):
    d = request.json
    print(gensql('insert','room_management.guest_service_status',d))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
def hotel_rm_post_Update_guestservicestatus(request):
    d = request.json
    a = { k : v for k,v in d.items()  if k in ('rm_room')}
    print(a)
    e = { k : v for k,v in d.items()  if k in ('rm_service_status')}
    gensql('update','room_management.guest_service_status',e,a)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

def hotel_rm_post_select_queryguestservicestatus(request):
       sql = json.loads(dbget("select guest_service_status.rm_service_status,rm_room_list.* from room_management.rm_room_list\
                           left join room_management.guest_service_status \
                           on  room_management.rm_room_list.rm_room = \
                           room_management.guest_service_status.rm_room where rm_room_list.rm_reservation_status in ('checkin')"))
 
       return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'ReturnCode':'RRTS'},indent=4))



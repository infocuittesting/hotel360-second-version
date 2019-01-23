from sqlwrapper import gensql,dbget, dbput
import json
def HOTEL_RES_POST_UPDATE_RoomMove(request):
    d = request.json
    res_id = d.get("Res_id")
    res_room = d.get("Res_room")
    res_unique_id = d.get("Res_unique_id")
    sql_value = dbget("select res_room,res_adults from reservation.res_reservation \
                       where res_id = '"+res_id+"' and res_unique_id = '"+res_unique_id+"' ")
    
    sql_value = json.loads(sql_value)
    print(sql_value)
    rm_room = str(sql_value[0]['res_room'])
    adult = str(sql_value[0]['res_adults'])
    print(adult,type(adult))
    print(rm_room,type(rm_room))
    rm_room  = rm_room.split(',')
    print(rm_room,type(rm_room))
    rm_room = str(rm_room)[1:-1]
    print(rm_room)
    fo_status = "vacant"
    res_status = "not reserved"
    #rm_hk_status = "vaccant"
    psql = dbput("update room_management.rm_room_list set rm_fo_status = '"+fo_status+"', \
                 rm_reservation_status = '"+res_status+"',rm_room_status = '"+str(d['old_room_status'])+"',\
                 rm_fo_person = '0' where rm_room = '"+str(d['Old_Room'])+"'")
    print(psql)
   # updatebill = dbput("update cashiering.billing_post set res_room = '"+str(d['Res_room'])+"' \
                           #   where res_id = '"+str(d['Res_id'])+"' and res_room = '"+str(d['Old_Room'])+"'")
    print("updatebill",updatebill)
    if len(sql_value) != 0:
          data = '0'
          psql = dbput("update reservation.res_reservation set res_room='"+data+"' \
                       where res_id = '"+res_id+"' and res_unique_id = '"+res_unique_id+"' ")
          print(psql)
          a,e = {},{}
          e['Res_id'] = res_id
          a['Res_room'] = res_room
          e['Res_unique_id'] = res_unique_id
          sql_value = gensql('update','reservation.res_reservation',a,e)
          rmove_room = a.get("Res_room")
          print(rmove_room)
          rmove_room  = rmove_room.split(',')
          print(rmove_room,type(rmove_room))
          rmove_room = str(rmove_room)[1:-1]
          print(rmove_room)
          
          fo_status = "occupied"
          res_status = "checkin"
          #rm_hk_status = "occupied"
          sql_value = dbput("update room_management.rm_room_list set rm_fo_status = '"+str(fo_status)+"',rm_reservation_status = '"+res_status+"',rm_fo_person = '"+adult+"' where rm_room in ("+rmove_room+")")
          print(sql_value)
          room_move = "Room Move from "+ rm_room + "to "+rmove_room
         
          return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','RoomMove':room_move ,'ReturnCode':'RUS'}, sort_keys=True, indent=4))


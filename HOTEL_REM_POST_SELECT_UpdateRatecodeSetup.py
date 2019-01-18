from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_REM_POST_SELECT_UpdateRatecodeSetup(request):
    d = request.json
    print(d)
    records,rec1,rec2,rec3,rec4,rec5 = [],[],[],[],[],[]

    records = json.loads(dbget("select ratecode_setup.rateheader_id, ratecode.ratecode_id,ratecode.rate_code,\
                                ratecode.rate_description,ratecategory.rate_category,ratecategory.rate_category_decription,\
                                ratecategory.ratecategory_id,ratecategory.rate_class,\
                                ratecode_setup.begin_sell_date,ratecode_setup.end_sell_date,market.id,\
                                market.marketgroup,market.marketgroup_description,res_source.id,\
                                res_source.sourcecode,res_source.sourcedescription,ratecode_setup.display_sequence,sell_control.*,rate_components.*,\
                                ratecode_setup.rooms_id,ratecode_setup.packages_id,tranction_details.*\
                                from revenue_management.ratecode_setup\
                                join revenue_management.ratecode on ratecode_setup.ratecode_id = ratecode.ratecode_id \
                                join revenue_management.ratecategory on ratecode.rate_category_id = ratecategory.ratecategory_id\
                                join reservation.market on ratecode_setup.market_id = market.id\
                                join reservation.res_source on ratecode_setup.source_id = res_source.id\
                                join revenue_management.sell_control on ratecode_setup.sell_control_id = sell_control.sell_id\
                                join revenue_management.rate_components on ratecode_setup.rate_components_id =\
                                rate_components.components_id join revenue_management.tranction_details on\
                                ratecode_setup.transaction_details_id = tranction_details.tranction_detail_id \
                                where ratecode_setup.ratecode_id="+str(d['ratecode_id'])+" "))
    #print(records[0]['rooms_id'])
    #print(records)
    if len(records) != 0:
      #if rec3[0]['rooms_id'] is not None:
        print("rooms")
        rec1 = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id, room_type.room_type_id,room_type.room_type \
                             from revenue_management.rooms_selected join revenue_management.room_type on \
                             rooms_selected.room_type_id = room_type.room_type_id \
                             where rooms_id ="+str(records[0]['rooms_id'])+""))

    #records.append({"room_types":rec1})
    #print(records[0]['packages_id'])
        #if rec3[0]['packages_id'] is not None:
        print("packages")
        rec2 = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id where packages_id="+str(records[0]['packages_id'])+" "))
    #records.append({"packages":rec2})

    rec3 = json.loads(dbget("SELECT rate_details_id, one_adult_amount, two_adult_amount, three_adult_amount,\
                             four_adult_amount, extra_adult_amount, one_child_amount, two_child_amount,\
                             extra_child_amount, start_date, end_date, season_code.*,rate_days.*,rate_details.ratecode_id,\
                             rate_details.rooms_id,rate_details.packages_id, \
                             rate_tier.* FROM revenue_management.rate_details \
                             join revenue_management.season_code on rate_details.season_code_id = \
                             season_code.season_code_id join revenue_management.rate_days on \
                             rate_details.rate_days_id = rate_days.rate_days_id left join revenue_management.rate_tier \
                             on rate_details.rate_tier_id = rate_tier.rate_tier_id where \
                             rate_details.ratecode_id="+str(d['ratecode_id'])+" "))
    print("rec3",rec3)
    if len(rec3) != 0:
      #if rec3[0]['rooms_id'] is not None:

       print("rooms")
       rec4 = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id, room_type.room_type_id,room_type.room_type \
                             from revenue_management.rooms_selected join revenue_management.room_type on \
                             rooms_selected.room_type_id = room_type.room_type_id \
                             where rooms_id ="+str(rec3[0]['rooms_id'])+""))
    #rec3.append({"room_types":rec4})
    #print(records[0]['packages_id'])
       if rec3[0]['packages_id'] is not None:
         print("packages")
         rec5 = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id where packages_id="+str(rec3[0]['packages_id'])+" "))
    #rec3.append({"packages":rec5})
    return(json.dumps({"Rate_header":records,"Rate_header_room_types":rec1,"Rate_header_packages":rec2,
                       "Rate_details":rec3,"Rate_details_room_types":rec4,"Rate_details_packages":rec5,
                       "Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_REM_POST_SELECT_SelectRatesetupAll(request):
    
    records = json.loads(dbget("select ratecode_setup.rateheader_id, ratecode.ratecode_id,ratecode.rate_code,\
                                ratecode.rate_description,ratecategory.rate_category,ratecategory.rate_category_decription,\
                                ratecategory.ratecategory_id,ratecategory.rate_class,\
                                ratecode_setup.begin_sell_date,ratecode_setup.end_sell_date,market.*,\
                                res_source.*,\
                                ratecode_setup.display_sequence,sell_control.*,rate_components.*,\
                                ratecode_setup.rooms_id,ratecode_setup.packages_id,tranction_details.*\
                                from revenue_management.ratecode_setup\
                                join revenue_management.ratecode on ratecode_setup.ratecode_id = ratecode.ratecode_id  \
                                join revenue_management.ratecategory on ratecode.rate_category_id = ratecategory.ratecategory_id \
                                join reservation.market on ratecode_setup.market_id = market.id \
                                join reservation.res_source on ratecode_setup.source_id = res_source.id \
                                join revenue_management.sell_control on ratecode_setup.sell_control_id = sell_control.sell_id \
                                join revenue_management.rate_components on ratecode_setup.rate_components_id = rate_components.components_id \
                                join revenue_management.tranction_details on ratecode_setup.transaction_details_id = \
                                tranction_details.tranction_detail_id "))
    
    #print("records   ",records,"len",len(records))
    
    for cords in records:
        
      cords['rooms'] = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id,\
                                        room_type.id,room_type.type\
                                        from revenue_management.rooms_selected join room_management.room_type on \
                                        rooms_selected.room_type_id = room_type.id where\
                                        rooms_selected.rooms_id='"+str(cords['rooms_id'])+"' "))
      
      #print("records   ",records,"len",len(records)) 
    
    
      cords['packages'] = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id  where packages_selected.packages_id='"+str(cords['packages_id'])+"'"))

      rate_details = json.loads(dbget("select * from revenue_management.rate_details \
                                       where ratecode_id='"+str(cords['ratecode_id'])+"'"))

      print("rate_details  ",rate_details, len(rate_details))
    
      for rate in rate_details:
          #print("rate",rate)
          detail_rate = json.loads(dbget("SELECT rates_all.rates_id, rates_all.ratecode_id, \
                                              rates_all.rate_details_id, season_code.*, rates_all.rate_date,\
                                              rates_all.one_adult_rate, rates_all.two_adult_rate, rates_all.three_adult_rate,\
                                              rates_all.four_adult_rate, rates_all.one_child_rate,rates_all.two_child_rate,\
                                              rates_all.extra_child_rate, rates_all.rooms_id, rates_all.packages_id,\
                                              rate_tier.* from revenue_management.rates_all join \
                                              revenue_management.season_code on \
                                              rates_all.season_code_id = season_code.season_code_id join \
                                              revenue_management.rate_tier on \
                                              rates_all.rate_tier_id = rate_tier.rate_tier_id \
                                              where rates_all.ratecode_id='"+str(rate['ratecode_id'])+"' "))[0]

          #print("rateof", detail_rate,type(detail_rate))
          
          #for r_details in detail_rate[0]:
            
              #print("roomno",r_details)
              #r_no = rate['details'][0]['rooms_id']
           
              
          x = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id,\
                                                           room_type.id as roomid,room_type.type as roomstype\
                                                           from revenue_management.rooms_selected  join room_management.room_type on \
                                                           rooms_selected.room_type_id = room_type.id \
                                                          where rooms_selected.rooms_id='"+str(detail_rate['rooms_id'])+"' "))
          rate['rooms'] = x
              
              
          y = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                                                              packages_codes.package_code,packages_codes.package_code_id\
                                                              from revenue_management.packages_selected\
                                                              join revenue_management.packages_codes on packages_selected.package_code_id =  \
                                                              packages_codes.package_code_id  where \
                                                              packages_selected.packages_id='"+str(detail_rate['packages_id'])+"'"))
          rate['packages'] = y

          detail_rate['rooms'] = x
          detail_rate['packages'] = y
          rate['advanced_details'] = detail_rate
          
      cords['rate_details'] = rate_details        
    #print("--------------------------------------")
    #print("records   ",records,"len",len(records))       
    return(json.dumps({"records":records,"return_code":"RRS","message":"Record Retrived Successfully"},indent=4))

    '''
    rec3 = json.loads(dbget("SELECT rate_details_id, one_adult_rate, two_adult_rate, three_adult_rate,\
                             four_adult_rate, extra_adult_rate, one_child_rate, two_child_rate,\
                             extra_child_rate, season_code.*,rates_all.ratecode_id,\
                             rates_all.rooms_id,rates_all.packages_id, \
                             rate_tier.* FROM revenue_management.rates_all \
                             join revenue_management.season_code on rates_all.season_code_id = \
                             season_code.season_code_id join revenue_management.rate_tier \
                             on rates_all.rate_tier_id = rate_tier.rate_tier_id "))

SELECT rates_all.rates_id, rates_all.ratecode_id, rates_all.rate_details_id, season_code.*, rates_all.rate_date, 
rates_all.one_adult_rate, rates_all.two_adult_rate, rates_all.three_adult_rate, rates_all.four_adult_rate, rates_all.one_child_rate, 
rates_all.two_child_rate, rates_all.extra_child_rate, rates_all.rooms_id, rates_all.packages_id, rates_all.rate_tier_id 
from revenue_management.rates_all join revenue_management.season_code on 
rates_all.season_code_id = season_code.season_code_id


    if len(rec3) != 0:

      rec4 = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id, room_type.room_type_id,room_type.room_type \
                             from revenue_management.rooms_selected join revenue_management.room_type on \
                             rooms_selected.room_type_id = room_type.room_type_id \
                             "))
    #rec3.append("room_types":rec4)
    #print(records[0]['packages_id'])
      rec5 = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id "))
    #rec3.append("packages":rec5)
    
    return(json.dumps({"Rate_header":records,"Rate_header_room_types":rec1,"Rate_header_packages":rec2,
                       "Rate_details":rec3,"Rate_details_room_types":rec4,"Rate_details_packages":rec5,
                       "Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))
    '''


#Input Param: Null
#OutputParam: Null
#Purpose: This root file pass the parameters value to another file
#Date: 13/03/18
#Author: Daisy



from flask import Flask,request, jsonify

#</------profile webservice-----------/>
from UpdateIndividualProfile import UpdateIndividualProfile
from UpdateCompanyProfile import UpdateCompanyProfile
from QueryProfileRecord import QueryProfileAcitivitylog
from QueryProfileRecord import QueryNegotiatedRate
from UpdateNegotiatedRate import UpdateNegotiatedRate
from UpdateProfileNotes import UpdateProfileNotes
from QueryProfileRecord import QueryProfileNotes
from UpdateProfilePreferencenew import UpdateProfilePreferencenew
from UpdateProfilePreference import UpdateProfilePreference
from UpdateProfileCreditcard import UpdateProfileCreditcard
from DeleteProfileRecord import DeleteProfileRecord
from QueryProfileRecord import QueryProfilePreference
from UpdateProfileCreditcardRecord import UpdateProfileCreditcardRecord
from UpdateProfileRecord import UpdateProfileRecord
from QueryProfileRecord import QueryProfileCreditcard
from UpdateProfileNotesRecord import UpdateProfileNotesRecord
from UpdateProfileNegotiatedRateRecord import UpdateProfileNegotiatedRateRecord
from MergeProfile import MergeProfile
from QueryProfileRecordAll import QueryProfileRecordAll
from profilesearch import QueryProfileSearch
from QueryProfileHistory import QueryProfileHistoryRecord
from QueryProfileHistory import QueryProfileStatistics
from QueryProfileHistory import QueryProfileFutureRecord
from UpdateCompanyProfile import UpdateCompanyProfileRecord
from UpdateCompanyProfile import UpdateIndividualProfileRecord
from UpdateProfileCreditcard import UpdateProfileCreditcardnew
#delete service
from DeleteProfileRecordAll import DeleteProfileCreditCard
from DeleteProfileRecordAll import DeleteProfileNegotiate
from DeleteProfileRecordAll import DeleteProfileNotes
from DeleteProfileRecordAll import DeleteProfilePreference
#dropdown select
from profilecity import profilecity
from profilecity import profilelanguage
from profilecity import profilecountry
from profilecity import profilestate
from profilecity import profilepostalcode
from profilecity import profilevip
from profilecity import profilenationality
from profilecity import profilecurrency
from profilecity import profilecommunication
from profilecity import profilepftype
from profilecity import profileratecode
from profilecity import profilenotetype
from profilecity import profilepreferencegroup
from profilecity import profilepreferencevalue
from profilecity import Title
#dropdown insert
from profileinsertvalue import profilecity_insert
from profileinsertvalue import profilelanguage_insert
from profileinsertvalue import profilecountry_insert
from profileinsertvalue import profilestate_insert
from profileinsertvalue import profilepostalcode_insert
from profileinsertvalue import profilevip_insert
from profileinsertvalue import profilenationality_insert
from profileinsertvalue import profilecurrency_insert
from profileinsertvalue import profilecommunication_insert
from profileinsertvalue import profilepftype_insert
from profileinsertvalue import profileratecode_insert
from profileinsertvalue import profilenotetype_insert
from profileinsertvalue import profilepreferencegroup_insert
from profileinsertvalue import profilepreferencevalue_insert
from profileinsertvalue import Title_insert

#</------profile webservice-------------------/>

#</--------------reservation webservice---------/>
from HOTEL_RES_POST_INSERT_UpdateNewReservation import HOTEL_RES_POST_INSERT_UpdateNewReservation
from HOTEL_RES_POST_UPDATE_UpdateReservation import HOTEL_RES_POST_UPDATE_UpdateReservation
from HOTEL_RES_POST_INSERT_UpdateFixedRateReservation import HOTEL_RES_POST_INSERT_UpdateFixedRateReservation
from HOTEL_RES_POST_UPDATE_UpdateFixedRateReservation import HOTEL_RES_POST_UPDATE_UpdateFixedRateReservation
from HOTEL_RES_POST_INSERT_WaitlistReservation import HOTEL_RES_POST_INSERT_WaitlistReservation
from HOTEL_RES_GET_SELECT_QueryWaitlistReservation import HOTEL_RES_GET_SELECT_QueryWaitlistReservation
from HOTEL_RES_POST_UPDATE_UpdateWaitlistReservation import HOTEL_RES_POST_UPDATE_UpdateWaitlistReservation
from HOTEL_RES_POST_INSERT_UpdateAlertReservation import HOTEL_RES_POST_INSERT_UpdateAlertReservation
from HOTEL_RES_GET_SELECT_QueryAlertReservation import HOTEL_RES_GET_SELECT_QueryAlertReservation
from HOTEL_RES_POST_UPDATE_UpdateReservationAlert import HOTEL_RES_POST_UPDATE_UpdateReservationAlert
from Hotel_RES_Get_Select_QueryReservationActivitylog import Hotel_RES_POST_Select_QueryReservationActivitylog
from Hotel_RES_Post_Insert_UpdateFixedChargesReservation import Hotel_RES_Post_Insert_UpdateFixedChargesReservation
from HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation import HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation
from HOTEL_RES_GET_SELECT_QueryFixedChargesReservation import HOTEL_RES_GET_SELECT_QueryFixedChargesReservation
from HOTEL_RES_POST_INSERT_UpdateDeposit import HOTEL_RES_POST_INSERT_UpdateDeposit
from HOTEL_RES_POST_UPDATE_UpdateDeposit import HOTEL_RES_POST_UPDATE_UpdateDeposit
from HOTEL_RES_GET_SELECT_QueryDepositrule import HOTEL_RES_GET_SELECT_QueryDepositrule
from HOTEL_RES_GET_SELECT_RoomUnassign import HOTEL_RES_GET_SELECT_RoomUnassign
from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Post_Insert_UpdateGuestPrivileges
from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Post_Update_UpdateGuestPrivileges
from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Get_Select_QueryGuestPrivileges
from Hotel_RES_Post_Insert_UpdateGuestTraces import Hotel_RES_Post_Insert_UpdateGuestTraces
from Hotel_RES_Post_Insert_UpdateGuestTraces import Hotel_RES_Post_Update_UpdateGuestTraces
from Hotel_RES_Post_Insert_UpdateGuestTraces import Hotel_RES_Get_Select_QueryGuestTraces
from HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation import HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation
from Hotel_RES_Post_Select_Queryreservation import hotel_res_post_select_queryreservation
from QueryReservationSearch import QueryReservationSearch
from HOTEL_RES_POST_SELECT_QueryHistoryReservation import QueryHistoryReservation
from HOTEL_RES_GET_SELECT_QueryFixedRateReservation import HOTEL_RES_GET_SELECT_QueryFixedRateReservation
from HOTEL_RES_POST_INSERT_CancelReservation import HOTEL_RES_POST_INSERT_CancelReservation
from HOTEL_RES_POST_INSERT_ReinstateReservation import HOTEL_RES_POST_INSERT_ReinstateReservation
from HOTEL_RES_POST_SELECT_QueryArrivalFromToReservation import HOTEL_RES_POST_SELECT_QueryArrivalFromToReservation
from HOTEL_RES_POST_INSERT_WaitlistReason import HOTEL_RES_POST_INSERT_WaitlistReason
from HOTEL_RES_POST_INSERT_AcceptWaitlistReservation import HOTEL_RES_POST_INSERT_AcceptWaitlistReservation
from HOTEL_RES_POST_INSERT_ReservationCreditcard import HOTEL_RES_POST_INSERT_ReservationCreditcard
from HOTEL_RES_POST_INSERT_ReservationCreditcard import Hotel_RES_Post_Update_UpdateReservationCreditcard
from HOTEL_RES_POST_INSERT_ReservationCreditcard import Hotel_RES_Get_Select_QueryReservationCreditcard
from HOTEL_RES_POST_DELETE_DeleteReservation import HOTEL_RES_POST_DELETE_DeleteReservation
from Hotel_RES_Post_Update_TracesResloved import Hotel_RES_Post_Update_TracesResloved
from HOTEL_RES_POST_UPDATE_RoomMove import HOTEL_RES_POST_UPDATE_RoomMove
from HOTEL_RES_POST_INSERT_ReservationCreditcard import Hotel_RES_POST_Delete_DeleteReservationCreditcard
from HOTEL_RES_POST_INSERT_UpdateDeposit import HOTEL_RES_POST_SELECT_QueryDeposit

from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Restype
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Alertarea
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Alertcode
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Origin
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Source
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Payment
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Market
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Department
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Transaction_code
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_depositrule
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_CancelReason
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Cardtype
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Waitlist_reason
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Privileges

from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_RestypeInsert
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Alertarea
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Alertcode
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Origin
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Source
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Payment
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Market
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Department
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Transaction_code
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Depositrule
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_CancelReason
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Cardtype
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Waitlist_reason
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Privileges

from Hotel_RES_POST_SELECT_QueryFutureReservation import ProfileFutureReservation
from HOTEL_RES_POST_INSERT_UpdateNewReservation import Reservationdonutchart
#pending webservice

from HOTEL_RES_POST_SELECT_QueryHistoryReservation import HOTEL_RES_POST_SELECT_RateQuery
from HOTEL_RES_POST_INSERT_AttachAcompanyingGuest import HOTEL_RES_POST_INSERT_AttachAcompanyingGuest
from HOTEL_RES_POST_INSERT_AttachAcompanyingGuest import HOTEL_RES_POST_INSERT_DetachAcompanyingGuest
from HOTEL_RES_POST_INSERT_AttachAcompanyingGuest import HOTEL_RES_POST_SELECT_QueryAccompanyingGuest
#from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Get_Select_privileges

from Hotel_RES_Post_Insert_UpdateFixedChargesReservation import Hotel_RES_Post_SELECT_QueryTransactioncodeCode
from Hotel_RES_Post_Insert_UpdateFixedChargesReservation import Hotel_RES_Post_SELECT_SelectFixedCharges
from HOTEL_RES_POST_INSERT_UpdateFixedRateReservation import HOTEL_RES_POST_SELECT_QueryFixedRateReservation
from Hotel_RES_Post_Update_TracesResloved import Hotel_RES_Post_Delete_RemoveTraces
from Hotel_RES_Post_Update_TracesResloved import Hotel_RES_Post_Select_PropertyCalendar
from HOTEL_RES_POST_INSERT_UpdateFixedRateReservation import HOTEL_RES_POST_SELECT_QueryRateInfo
from HOTEL_RES_POST_SELECT_QueryPackageOptions import HOTEL_RES_POST_SELECT_QueryPackageOptions
from HOTEL_RES_POST_Insert_RoomRouting import HOTEL_RES_POST_Insert_RoomRouting
from HOTEL_RES_POST_Insert_RoomRouting import Hotel_RES_Get_Select_QueryRoomRouting
from HOTEL_RES_POST_SELECT_QueryHistoryReservation import HOTEL_RES_POST_select_Paticularreservation
#<--------------------------BUSINESS BLOCK DROPDOWN---------------------------->
#from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Block_status

#</--------------reservation webservice---------/>
#<-------------------Frontdesk------------------>
from HOTEL_FD_POST_INSERT_UpdateQueueRreservation import HOTEL_FD_POST_INSERT_UpdateQueueRreservation
from HOTEL_FD_GET_SELECT_QueryQueueReservation import HOTEL_FD_POST_SELECT_QueryQueueReservation
from HOTEL_FD_POST_INSERT_RoomAssign import HOTEL_FD_POST_UPDATE_RoomAssign
from HOTEL_FD_GET_SELECT_QueryTracesActivityLog import HOTEL_FD_GET_SELECT_QueryTracesActivityLog
from HOTEL_FD_POST_UPDATE_CheckinGuestArrivals import HOTEL_FD_POST_UPDATE_CheckinGuestArrivals
from HOTEL_FD_POST_SELECT_QueryRoomAssignment import HOTEL_FD_POST_SELECT_QueryRoomAssignment
from HOTEL_FD_GET_SELECT_QueryTracesActivityLog import HOTEL_FD_GET_SELECT_QueryNotes
from HOTEL_FD_GET_SELECT_QueryTracesActivityLog import HOTEL_FD_GET_SELECT_Querypreference
#<--------------------------------------------------->
#<---------------Room management------------------------->
from Hotel_RM_Post_Insert_Updateroom import hotel_rm_post_insert_updateroomlist
from Hotel_RM_Post_Update_Updateroomstatus import Hotel_Rm_Post_Update_Updateroomstatus
from Hotel_Rm_Post_Select_QueryRoomList import hotel_rm_post_select_queryroomlist
from Hotel_Rm_Post_Select_QueryroomStatistics import hotel_rm_post_select_queryroomstatistics
from Hotel_RM_Post_Insert_Updateroom import hotel_rm_post_insert_updateroomcondition
from Hotel_Rm_Post_Select_QueryRoomCondition import hotel_rm_post_select_queryroomcondition
from Hotel_Rm_Post_Select_QueryRoomCondition import hotel_rm_post_delete_roomcondition
from Hotel_RM_Post_Update_Updateroomdiscrepancies import hotel_rm_post_update_updateroomdiscrepancies
from Hotel_Rm_Post_Select_QueryRoomDiscrepancies import hotel_rm_post_select_queryroomdiscrepancies
from Hotel_Rm_Post_Insert_UpdateGuestServiceStatus import hotel_rm_post_insert_updateguestservicestatus
from Hotel_Rm_Post_Insert_UpdateGuestServiceStatus import hotel_rm_post_select_queryguestservicestatus
from Hotel_RM_Post_Insert_Updateroom import hotel_rm_post_insert_updateoutoforderservice
from Hotel_RM_Post_Select_Queryoutoforderservice import hotel_rm_post_select_queryoutoforderservice
from Hotel_RM_Post_Insert_Updateroom import hotel_rm_post_insert_updateroommaintenance
from Hotel_RM_Post_Insert_Updateroom import hotel_rm_post_update_resolveroommaintenance
from Hotel_RM_Post_Select_Queryroommaintenance import hotel_rm_post_select_queryroommaintenance

from Hotel_RM_Post_Select_Queryroommaintenance import hotel_rm_post_delete_deleteroommaintenance
from Hotel_Rm_Post_Update_UpdateRoomCondition import hotel_rm_post_update_updateroomcondition
from Hotel_RM_Post_Select_Queryoutoforderservice import hotel_rm_post_update_updateoutoforderservice

#pending webservice
from Hotel_RM_Post_SELECT_OccupancyGraph import Hotel_RM_Post_SELECT_OccupancyGraph
from Hotel_Rm_Post_Insert_UpdateGuestServiceStatus import hotel_rm_post_Update_guestservicestatus
from Hotel_RM_Post_Select_Queryroommaintenance import hotel_rm_post_select_OutoforderRoomsonly
from hotel_rm_post_Select_Turndown_management import hotel_rm_post_Select_Turndown_management
from Hotel_RM_Post_SELECT_OccupancyGraph import Hotel_RM_Post_SELECT_FacilityForecast
from hotel_rm_post_Select_Turndown_management import hotel_rm_post_update_Turndown_management
from hotel_rm_post_Select_Turndown_management import hotel_rm_post_select_Dropdown_Turndown_management

from RoomManagementDropdown import select_roomstatus
from RoomManagementDropdown import select_class
from RoomManagementDropdown import select_condition
from RoomManagementDropdown import select_hkstatus_code
from RoomManagementDropdown import select_room_type
from RoomManagementDropdown import select_room_no
from RoomManagementDropdown import select_discription
from RoomManagementDropdown import select_servicestatus_code
from RoomManagementDropdown import select_turndownstatus
from RoomManagementDropdown import select_room_service_status
from RoomManagementDropdown import select_mainteanance_reason
from RoomManagementDropdown import select_floor
#insert

from RoomManagementDropdownInsert import insert_roomstatus
from RoomManagementDropdownInsert import insert_class
from RoomManagementDropdownInsert import insert_condition
from RoomManagementDropdownInsert import insert_hkstatus_code
from RoomManagementDropdownInsert import insert_room_type
from RoomManagementDropdownInsert import insert_room_no
from RoomManagementDropdownInsert import insert_room_discription
from RoomManagementDropdownInsert import insert_servicestatus_code
from RoomManagementDropdownInsert import insert_turndownstatus
from RoomManagementDropdownInsert import insert_room_service_status
from RoomManagementDropdownInsert import insert_mainteanance_reason
from RoomManagementDropdownInsert import insert_floor
#<------------------------------------------------------------------->
#<----------------------REVENUE MANAGEMENT--------------------------->
from HOTEL_REVENUE_MANAGEMENT_POST_INSERT_RATECATEGORY import ratecategory
from HOTEL_REVENUE_MANAGEMENT_POST_INSERT_RATECATEGORY import ratecode
from HOTEL_REVENUE_MANAGEMENT_POST_INSERT_RATECATEGORY import market
from HOTEL_REVENUE_MANAGEMENT_POST_INSERT_RATECATEGORY import sourcetab
from HOTEL_REVENUE_MANAGEMENT_POST_INSERT_RATECATEGORY import crrencytab
from HOTEL_REVENUE_MANAGEMENT_POST_SELECT import rateselect
from HOTEL_REVENUE_MANAGEMENT_POST_SELECT import ratecodeselect
from HOTEL_REVENUE_MANAGEMENT_POST_SELECT import marketselect
from HOTEL_REVENUE_MANAGEMENT_POST_SELECT import sourceselect
from HOTEL_REVENUE_MANAGEMENT_POST_SELECT import currencyselect
from HOTEL_REVENUE_MANAGEMENT_POST_INSERT_RATECATEGORY import negotiated
from HOTEL_REVENUE_MANAGEMENT_POST_INSERT_RATECATEGORY import ratedetailss
from HOTEL_REM_POST_INSERT_UpdateRatecodeSetup import HOTEL_REM_POST_INSERT_UpdateRatecodeSetup
from HOTEL_REM_POST_SELECT_QueryRatecode import HOTEL_REM_POST_SELECT_QueryRatecode

from HOTEL_REVENUE_MANAGEMENT_POST_SELECT import room_types
from HOTEL_REVENUE_MANAGEMENT_POST_SELECT import packages_revenue
from HOTEL_REVENUE_MANAGEMENT_POST_SELECT import season_code_revenue
from HOTEL_REVENUE_MANAGEMENT_POST_SELECT import Insert_season_code_revenue
from HOTEL_REM_POST_INSERT_UpdateRatecodeSetup import HOTEL_REM_POST_SELECT_Ratecode
from HOTEL_REM_POST_INSERT_UpdateRatecodeSetup import HOTEL_REM_POST_SELECT_Negotiated_Rate
from HOTEL_REM_POST_DELETE import Delete_Negotiated_Rate
from HOTEL_REM_POST_UPDATE_UpdateRatecodeSetup import HOTEL_REM_POST_UPDATE_UpdateRatecodeSetup
from HOTEL_REM_POST_SELECT_UpdateRatecodeSetup import HOTEL_REM_POST_SELECT_UpdateRatecodeSetup
from HOTEL_REM_POST_UPDATE_UpdateRatecodeSetup import HOTEL_REM_POST_UPDATE_Negotiated_Rate
from HOTEL_REM_POST_SELECT_UpdateRatecodeSetup import HOTEL_REM_POST_SELECT_SelectRatesetupAll
from HOTEL_REM_POST_UPDATE_UpdateRatecodeSetup import HOTEL_REM_POST_UPDATE_RATE_DETAILS
from HOTEL_REM_POST_DELETE import Delete_Rate_code
from HOTEL_REM_POST_DELETE import Delete_Rate_details


#<----------------------------------------Cashiering-------------------------->
from HOTEL_CAH_POST_INSERT_UPDATEGUESTBILLING import HOTEL_CAH_POST_INSERT_UPDATEGUESTBILLING
from HOTEL_CAH_POST_UPDATE_UPDATEGUESTBILLING import HOTEL_CAH_POST_UPDATE_UPDATEGUESTBILLING
from HOTEL_CAH_GET_SELECT_QUERYGUESTBILLING import HOTEL_CAH_POST_SELECT_QUERYGUESTBILLING
from HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENT import HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENT
from HOTEL_CAH_POST_POSTING_HISTORY_LOG import HOTEL_CAH_POST_POSTING_HISTORY_LOG
from HOTEL_CAH_POST_FOLIO_HISTORY import HOTEL_CAH_POST_FOLIO_HISTORY
from HOTEL_CAH_POST_UPDATE_TransfertoAnotherWindow import HOTEL_CAH_POST_UPDATE_TransfertoAnotherWindow
from HOTEL_CASH_BILLING_CODE_INSERT import HOTEL_CASH_BILLING_CODE_INSERT
from HOTEL_CASH_BILLING_CODE_SELECT import HOTEL_CASH_BILLING_CODE_SELECT
from HOTEL_CASH_INSERT_BILLING_CURRENCY import HOTEL_CASH_INSERT_BILLING_CURRENCY
from HOTEL_CASH_SELECT_POSTING_WINDOW import HOTEL_CASH_SELECT_POSTING_WINDOW
from HOTEL_CASH_RESERVATION_BALANCE import HOTEL_CASH_RESERVATION_BALANCE
from HOTEL_CASH_RESERVATION_STATUS import HOTEL_CASH_RESERVATION_STATUS
from HOTEL_CAH_POST_UPDATE_TransfertoAnotherRoom import HOTEL_CAH_POST_UPDATE_TransfertoAnotherRoom
from HOTEL_CAH_POST_CASH_CHECK_OUT import HOTEL_CAH_POST_CASH_CHECK_OUT
from HOTEL_CAH_POST_POSTING_PAYMENT import HOTEL_CAH_POST_POSTING_PAYMENT
from HOTEL_CAH_POST_POSTING_PAYMENT_INSERT import HOTEL_CAH_POST_POSTING_PAYMENT_INSERT
from HOTEL_CAH_GET_SELECT_QUERYINSHOUSERECORD import HOTEL_CAH_POST_SELECT_QUERYINHOUSERECORD

from HOTEL_CASH_BILLING_CODE_SELECT import HOTEL_CASH_PAYMENT_CODE_SELECT
from HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENT import HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENTCHECKOUT
#<-------------------------------------------------------------------------------------------------->
#<-----------------------Business Block---------------------------------------------------------->
from HOTEL_BBL_POST_INSERT_BusinessBlock import HOTEL_BBL_POST_INSERT_BusinessBlock
from HOTEL_BBL_POST_UPDATE_Business_Block_Update import HOTEL_BBL_POST_UPDATE_Business_Block_Update
from HOTEL_BBL_POST_INSERT_Business_Block_Notes import HOTEL_BBL_POST_INSERT_Business_Block_Notes
from HOTEL_BBL_POST_INSERT_Business_Block_Notes import HOTEL_BBL_POST_SELECT_Business_Block_Notes
from HOTEL_BBL_POST_INSERT_GroupCancel import HOTEL_BBL_POST_INSERT_GroupCancel
from HOTEL_BBL_GET_SELECT_BusinessBlockSearch import HOTEL_BBL_GET_SELECT_BusinessBlockSearch
from HOTEL_BBL_POST_SELECT_Business_Block_activitylog import HOTEL_BBL_POST_SELECT_Business_Block_activitylog
from HOTEL_BBL_POST_SELECT_QueryGroupCancel import HOTEL_BBL_POST_SELECT_QueryGroupCancel
from HOTEL_BBL_POST_INSERT_BusinessBlockDefinite import HOTEL_BBL_POST_INSERT_BusinessBlockDefinite
from HOTEL_BBL_POST_INSERT_GroupReservation import HOTEL_BBL_POST_INSERT_GroupReservation
from HOTEL_BBL_POST_INSERT_BusinessBlock import HOTEL_BBL_POST_SELECT_QueryInquiryGrid
from HOTEL_BBL_POST_UPDATE_BusinessBlockStatus import HOTEL_BBL_POST_UPDATE_BusinessBlockStatus
from HOTEL_BBL_POST_INSERT_Grid import HOTEL_BBL_POST_INSERT_Grid
from HOTEL_BBL_POST_SELECT_QueryGrid import HOTEL_BBL_POST_SELECT_QueryGrid
from HOTEL_BBL_POST_UPDATE_UpdateGrid import HOTEL_BBL_POST_UPDATE_UpdateGrid
from HOTEL_BBL_POST_INSERT_CalculateRoomRevenue import HOTEL_BBL_POST_INSERT_CalculateRoomRevenue
from HOTEL_BBL_POST_SELECT_QueryRoomRevenue import HOTEL_BBL_POST_SELECT_QueryRoomRevenue
from HOTEL_BBL_POST_UPDATE_BusinessBlockDefinite import HOTEL_BBL_POST_UPDATE_BusinessBlockDefinite
from HOTEL_BBL_POST_INSERT_PayMasterReservation import HOTEL_BBL_POST_SELECT_QueryPayMasterReservation
from HOTEL_BBL_POST_INSERT_GroupReservation import HOTEL_BBL_POST_SELECT_QueryGroupReservation
#from HOTEL_BBL_POST_INSERT_GroupReservation import HOTEL_BBL_POST_INSERT_GroupReservation
from HOTEL_BBL_POST_INSERT_PayMasterReservation import HOTEL_BBL_POST_INSERT_PayMasterReservation
from HOTEL_BBL_POST_INSERT_PayMasterReservation import HOTEL_BBL_POST_SELECT_QueryPayMasterReservation
from HOTEL_BBL_POST_SELECT_EditBusinessBlockSearch import HOTEL_BBL_POST_SELECT_EditBusinessBlockSearch
from HOTEL_BBL_POST_UPDATE_UpdateGrid import HOTEL_BBL_POST_SELECT_SelectRoomingList_Roomtype
from HOTEL_BBL_POST_UPDATE_UpdateGrid import HOTEL_BBL_POST_UPDATE_UpdateRoomingList_Roomtype
from HOTEL_BBL_POST_UPDATE_UpdateGrid import HOTEL_BBL_POST_SELECT_SelectRoomtype
from HOTEL_BBL_POST_UPDATE_UpdateGrid import HOTEL_BBL_POST_SELECT_gridservice
#<--------------------------------------------------------------------------------------------->
#<---------------------business block dropdown--------------------------------------->
from HOTEL_BBL_GET_SELECT_QueryDrodown import HOTEL_BBL_GET_SELECT_BusinessBlockStatus
from HOTEL_BBL_GET_SELECT_QueryDrodown import HOTEL_BBL_GET_SELECT_InventoryContrtol
from HOTEL_BBL_GET_SELECT_QueryDrodown import HOTEL_BBL_GET_SELECT_MeetingSpaceType
from HOTEL_BBL_GET_SELECT_QueryDrodown import HOTEL_BBL_GET_SELECT_Block_Type

from HOTEL_BBL_GET_SELECT_QueryDrodown import HOTEL_BBL_POST_INSERT_BusinessBlockStatus
from HOTEL_BBL_GET_SELECT_QueryDrodown import HOTEL_BBL_POST_INSERT_InventoryContrtol
from HOTEL_BBL_GET_SELECT_QueryDrodown import HOTEL_BBL_POST_INSERT_MeetingSpaceType
from HOTEL_BBL_GET_SELECT_QueryDrodown import HOTEL_BBL_POST_INSERT_Block_Type

#<---------------------Packages------------------------------->
from HOTEL_PAC_POST_INSERT_Package_dropdowns import HOTEL_PAC_POST_INSERT_Forecastgroup
from HOTEL_PAC_POST_INSERT_Package_dropdowns import HOTEL_PAC_POST_INSERT_Transactioncode
from HOTEL_PAC_POST_INSERT_Package_dropdowns import HOTEL_PAC_POST_INSERT_Attributes
from HOTEL_PAC_POST_INSERT_Package_dropdowns import HOTEL_PAC_POST_INSERT_Postingrhythm
from HOTEL_PAC_POST_INSERT_Package_dropdowns import HOTEL_PAC_POST_INSERT_Calculaterule
from HOTEL_PAC_POST_INSERT_Package_dropdowns import HOTEL_PAC_POST_INSERT_Iteminventory
from HOTEL_PAC_POST_SELECT_Package_dropdowns import HOTEL_PAC_POST_SELECT_Forecastgroup
from HOTEL_PAC_POST_SELECT_Package_dropdowns import HOTEL_PAC_POST_SELECT_Transactioncode
from HOTEL_PAC_POST_SELECT_Package_dropdowns import HOTEL_PAC_POST_SELECT_Postingrhythm
from HOTEL_PAC_POST_SELECT_Package_dropdowns import HOTEL_PAC_POST_SELECT_Calculaterule
from HOTEL_PAC_POST_SELECT_Package_dropdowns import HOTEL_PAC_POST_SELECT_Iteminventory
from HOTEL_PAC_POST_INSERT_Package_Code import HOTEL_PAC_POST_INSERT_Packages
from HOTEL_PAC_POST_INSERT_Package_Code import HOTEL_PAC_POST_INSERT_Packagesdetails
from HOTEL_PAC_POST_UPDATE_Package_Code import HOTEL_PAC_POST_UPDATE_Packages
from HOTEL_PAC_POST_SELECT_Package_dropdowns import HOTEL_PAC_POST_SELECT_Packages
from HOTEL_PAC_POST_SELECT_Package_dropdowns import HOTEL_PAC_POST_SELECT_Packages_All
from HOTEL_PAC_POST_DELETE_Package_Code import HOTEL_PAC_POST_DELETE_Package
from HOTEL_PAC_POST_DELETE_Package_Code import HOTEL_PAC_POST_DELETE_Packagedetails
from HOTEL_PAC_POST_SELECT_Package_dropdowns import HOTEL_PAC_POST_SELECT_PackagesTrasnactioncode
#<--------------------------------------------------------------------->
#<---------------------------------amazonlex---------->
from AMAZON_RESERVATION_LAMBDA_LEX import AMAZON_RESERVATION_LAMBDA_LEX
from AMAZON_RESERVATION_LAMBDA_LEX import amazon_insert
from AMAZON_RESERVATION_LAMBDA_LEX import CheckConfirmation
from AMAZON_RESERVATION_LAMBDA_LEX import checkinguest
from AMAZON_RESERVATION_LAMBDA_LEX import Checkroom
from AMAZON_RESERVATION_LAMBDA_LEX import callexternalapi
#<----------------------------Acccount Receivable--------------------------------->
from HOTEL_AR_POST_INSERT_AccountSetup import HOTEL_AR_POST_INSERT_AccountSetup
from HOTEL_AR_POST_INSERT_AccountSetup import HOTEL_AR_POST_UPDATE_AccountSetup
from HOTEL_AR_POST_INSERT_AccountSetup import HOTEL_AR_POST_SELECT_AccountSetup
from HOTEL_AR_POST_INSERT_AccountSetup import HOTEL_AR_POST_DELETE_AccountSetup
from HOTEL_AR_POST_INSERT_ArNotes import HOTEL_AR_POST_INSERT_ArNotes
from HOTEL_AR_POST_INSERT_ArNotes import HOTEL_AR_POST_UPDATE_ArNotes
from HOTEL_AR_POST_INSERT_ArNotes import HOTEL_AR_POST_SELECT_ArNotes
from HOTEL_AR_POST_INSERT_ArNotes import HOTEL_AR_POST_DELETE_ArNotes
#from HOTEL_AR_POST_SELECT_ArPostHistory import HOTEL_AR_POST_SELECT_ArPostHistory
from HOTEL_AR_POST_INSERT_Account_Traces import HOTEL_AR_POST_INSERT_AccountTraces
from HOTEL_AR_POST_INSERT_Account_Traces import HOTEL_AR_POST_UPDATE_AccountTraces
from HOTEL_AR_POST_INSERT_Account_Traces import HOTEL_AR_POST_SELECT_AccountTraces
from HOTEL_AR_POST_INSERT_Account_Traces import HOTEL_AR_POST_DELETE_AccountTraces
from HOTEL_AR_POST_INSERT_AccountInvoice import HOTEL_AR_POST_INSERT_AccountInvoice
from HOTEL_AR_POST_INSERT_AccountInvoice import HOTEL_AR_POST_SELECT_AccountInvoice
from HOTEL_AR_POST_INSERT_AccountInvoice import HOTEL_AR_POST_DELETE_AccountInvoice
#from Night_audit_posting import Night_audit_posting
from HOTEL_AR_POST_INSERT_AccountInvoice import HOTEL_AR_POST_INSERT_Billingpost
from HOTEL_AR_POST_INSERT_AccountInvoice import HOTEL_AR_POST_SELECT_Billingpost
from HOTEL_AR_POST_INSERT_AccountInvoice import HOTEL_AR_POST_UPDATE_AdjustBillingpost
from HOTEL_AR_POST_INSERT_AccountInvoice import HOTEL_AR_POST_INSERT_Billingpayment
from HOTEL_AR_POST_SELECT_Activitylog import HOTEL_AR_POST_SELECT_AccountPostHistory
from HOTEL_AR_POST_SELECT_Activitylog import HOTEL_AR_POST_SELECT_AccountPayHistory


from HOTEL_AR_POST_SELECT_Activitylog import HOTEL_AR_POST_SELECT_ApplyPaymentSelectiviely
from HOTEL_AR_POST_SELECT_Activitylog import HOTEL_AR_POST_INSERT_UNApplyPayment
from HOTEL_AR_POST_SELECT_Activitylog import HOTEL_AR_POST_SELECT_ReversePayment
from HOTEL_AR_POST_SELECT_Activitylog import HOTEL_AR_POST_SELECT_UnappyPayment
from HOTEL_AR_POST_INSERT_CompressInvoice import HOTEL_AR_POST_INSERT_CompressInvoice
from HOTEL_AR_POST_INSERT_CompressInvoice import HOTEL_AR_POST_DELETE_UnCompressInvoice
from HOTEL_AR_POST_INSERT_CompressInvoice import HOTEL_AR_POST_SELECT_YearViewAmount
from HOTEL_AR_POST_INSERT_ReasonDropdown import HOTEL_AR_POST_INSERT_Account_typeDropdown
from HOTEL_AR_POST_INSERT_ReasonDropdown import HOTEL_AR_POST_SELECT_Account_typeDropdown
from HOTEL_AR_POST_INSERT_ReasonDropdown import HOTEL_AR_POST_INSERT_REASONDropdown
from HOTEL_AR_POST_INSERT_ReasonDropdown import HOTEL_AR_POST_SELECT_REASONDropdown
from HOTEL_AR_POST_INSERT_ARTransfer import HOTEL_AR_POST_INSERT_ARTransfer
from HOTEL_AR_POST_INSERT_ReasonDropdown import HOTEL_AR_POST_SELECT_InvoicePaymentDropdown
from HOTEL_AR_POST_INSERT_ReasonDropdown import HOTEL_AR_POST_INSERT_InvoicePaymentDropdown
from HOTEL_AR_POST_INSERT_ReasonDropdown import HOTEL_AR_POST_SELECT_AccountTypeDropdown
#<--------------------------------------------------------------------------------->


#<--------------------------------End of day-------------------------------------------->
from Hotel_END_OF_Day_POST_countrycheck import Hotel_END_OF_Day_POST_countrycheck
from Hotel_END_OF_Day_POST_countrycheck import Hotel_END_OF_Day_POST_Departure_Not_Checkedout
from Hotel_END_OF_Day_POST_countrycheck import Hotel_END_OF_Day_POST_Roll_Business_date
from Hotel_END_OF_Day_POST_countrycheck import Hotel_END_OF_Day_POST_Posting_Rooms_charges
from Hotel_END_OF_Day_POST_countrycheck import Hotel_END_OF_Day_POST_Run_Additional_procedures
from Hotel_END_OF_Day_POST_countrycheck import Hotel_END_OF_Day_POST_print_final_report
#<-----------------------------PMS Report------------------------------>
from Hotelpmsreport import GetReservationReport
from Hotelpmsreport import GetFrontDeskReport
from Hotelpmsreport import GetBusinessBlock
from Hotelpmsreport import GetProfileReport
from Hotelpmsreport import GetRoomHousekeeping
from Hotelpmsreport import GetFrontofficestatus
from Hotelpmsreport import GetRoomconditionall
from Hotelpmsreport import GetRoomDiscrepencies
from Hotelpmsreport import GetGuestServiceStatus
from Hotelpmsreport import GetZerobalanceaccount
from Hotelpmsreport import GetReservationNoshowreport
from Hotelpmsreport import futurebooking
from Hotelpmsreport import HistoryBooking
from Hotelpmsreport import Cashiergettotalamount
from Hotelpmsreport import RoomHistory

#<----------------------------------MERGE MODULE-------------------------------.
from HOTEL_PMS_SELECT_MergeModule import Hotel_PMS_Select_GetTodayRoomAvailabilityArrival
from HOTEL_PMS_SELECT_MergeModule import Hotel_PMS_cancel_DepositRuleReservation
from HOTEL_PMS_SELECT_MergeModule import Hotel_PMS_Select_BlockFollowupDecisiondate
from HOTEL_PMS_SELECT_MergeModule import Hotel_PMS_Select_Blockcutoffdatecutoffdays
from HOTEL_PMS_SELECT_MergeModule import Hotel_PMS_Select_DepositDueDate
from HOTEL_PMS_SELECT_MergeModule import Hotel_PMS_Select_Roominglistdue_date
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
#Review , include comment
#Post Method to invoke JSON POST Request
#<------profile route ---->
@app.route("/")
def index():
   return "welcome to smartmo"
@app.route("/Profile/UpdateIndividualProfile",methods = ['POST'])
def CreateIndividualProfile():
   return UpdateIndividualProfile(request)

@app.route("/Profile/UpdateCompanyProfile",methods = ['POST'])
def CreateCompanyProfile():
   return UpdateCompanyProfile(request)

@app.route("/Profile/QueryProfileAcitivitylog",methods=['POST'])
def queryprofilelog():
   return QueryProfileAcitivitylog(request)

@app.route("/Profile/QueryNegotiatedRate",methods=['POST'])
def querynegotiatedrate():
   return QueryNegotiatedRate(request)

@app.route("/Profile/UpdateNegotiatedRate",methods=['POST'])
def InsertNegotiatedRate():
   return UpdateNegotiatedRate(request)

@app.route("/Profile/UpdateProfileNotes", methods=['POST'])
def ProfileNotes():
   return UpdateProfileNotes(request)

@app.route("/Profile/QueryProfileNotes",methods=['POST'])
def querynotes():
   return QueryProfileNotes(request)

@app.route("/Profile/UpdateProfilePreferencenew",methods=['POST'])
def newprofilepreference():
   return UpdateProfilePreferencenew(request)

@app.route("/Profile/UpdateProfilePreference",methods=['POST'])
def UpdateGuestPreference():
   return UpdateProfilePreference(request)

@app.route("/Profile/UpdateProfileCreditcard", methods=['POST'])
def Updateprofilecreditcard():
   return UpdateProfileCreditcard(request)

@app.route("/Profile/DeleteProfileRecord",methods=['POST'])
def deleteprofile():
   return DeleteProfileRecord(request)

@app.route("/Profile/QueryProfilePreference",methods=['POST'])
def profilepreference():
   return QueryProfilePreference(request)

@app.route("/Profile/UpdateProfileCreditcardRecord",methods=['POST'])
def updatecreditcard():
   return UpdateProfileCreditcardRecord(request)

@app.route("/Profile/UpdateProfileRecord",methods=['POST'])
def updateIndividual():
   return UpdateProfileRecord(request)

@app.route("/Profile/QueryProfileCreditcard",methods=['POST'])
def querycreditcard():
   return QueryProfileCreditcard(request)

@app.route("/Profile/UpdateProfileNotesRecord",methods=['POST'])
def updateprofilenotes():
   return UpdateProfileNotesRecord(request)

@app.route("/Profile/UpdateProfileNegotiatedRateRecord",methods=['POST'])
def updatenegotiatedrate():
   return UpdateProfileNegotiatedRateRecord(request)

@app.route("/profile/MergeProfile",methods=['POST'])
def mergeprofilerecord():
   return MergeProfile(request)
@app.route("/profile/QueryProfileRecordAll",methods=['POST'])
def queryallrecord():
   return QueryProfileRecordAll(request)

@app.route("/Profile/QueryProfileSearch",methods=['GET'])
def ProfileSearch():
   return QueryProfileSearch(request)

@app.route("/Profile/QueryProfileHistory",methods=['POST'])
def QueryProfileHistory():
   return QueryProfileHistoryRecord(request)

@app.route("/Profile/QueryProfileStatistics",methods=['POST'])
def QueryProfileStatisticsRecord():
   return QueryProfileStatistics(request)

@app.route("/Profile/QueryFutureReservation",methods=['POST'])
def QueryProfileFuture():
   return QueryProfileFutureRecord(request)

@app.route("/Profile/UpdateCompanyProfileRecord",methods=['POST'])
def CompanyProfile():
   return UpdateCompanyProfileRecord(request)

@app.route("/Profile/UpdateIndividualProfileRecord",methods=['POST'])
def UpdateProfile():
   return UpdateIndividualProfileRecord(request)

@app.route("/Profile/UpdateProfileCreditcardnew",methods=['POST'])
def ProfileCreditcardnew():
   return UpdateProfileCreditcardnew(request)


#delete
@app.route("/Profile/DeleteProfileCreditcard",methods=['POST'])
def DeleteProfileCreditcard():
   return DeleteProfileCreditCard(request)

@app.route("/Profile/DeleteProfileNegotiate",methods=['POST'])
def DeleteProfileNegotiatedRate():
   return DeleteProfileNegotiate(request)

@app.route("/Profile/DeleteProfileNotes",methods=['POST'])
def DeleteProfileNote():
   return DeleteProfileNotes(request)

@app.route("/Profile/DeleteProfilePreference",methods=['POST'])
def DeleteProfilePreferences():
   return DeleteProfilePreference(request)

# select profile dropdown
@app.route("/Profile/profilecity",methods=['GET'])
def cityvalue():
   return profilecity()
@app.route("/Profile/profilelanguage",methods=['GET'])
def languagevalue():
   return profilelanguage()
@app.route("/Profile/profilecountry",methods=['GET'])
def countryvalue():
   return profilecountry()
@app.route("/Profile/profilestate", methods=['GET'])
def statevalue():
   return profilestate()
@app.route("/Profile/profilepostalcode",methods=['GET'])
def postalcodevalue():
   return profilepostalcode()
@app.route("/Profile/profilevip",methods=['GET'])
def profilevivalue():
   return profilevip()
@app.route("/Profile/profilenationality",methods=['GET'])
def profilenationalityvalue():
   return profilenationality()
@app.route("/Profile/profilecurrency",methods=['GET'])
def profilecurrencyvalue():
   return profilecurrency()
@app.route("/Profile/profilecommunication",methods=['GET'])
def profilecommunicationvalue():
   return profilecommunication()
@app.route("/Profile/profilepftype",methods=['GET'])
def profilepftypevalue():
   return profilepftype()
@app.route("/Profile/profileratecode",methods=['GET'])
def profileratecodevalue():
   return profileratecode()
@app.route("/Profile/profilenotetype",methods=['GET'])
def profilenotetypevalue():
   return profilenotetype()
@app.route("/Profile/profilepreferencegroup",methods=['GET'])
def profilepreferencegroupvalue():
   return profilepreferencegroup()
@app.route("/Profile/profilepreferencevalue",methods=['GET'])
def profilepreferencevalues():
   return profilepreferencevalue()
@app.route("/Profile/Title",methods=['GET'])
def tiltledf():
   return Title()

@app.route("/Profile/Title_insert",methods=['POST'])
def tiltledSDFDf():
   return Title_insert(request)
#<----------------------------------------------------------->

#</----------------reservation route--------->
@app.route("/Hotel_RES_Post_Insert_UpdateFixedChargesReservation",methods=['POST'])
def insertfixedcharges():
    return Hotel_RES_Post_Insert_UpdateFixedChargesReservation(request)

@app.route("/HOTEL_RES_POST_INSERT_UpdateNewReservation",methods=['POST'])
def CreateNewReservation():
    return HOTEL_RES_POST_INSERT_UpdateNewReservation(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateReservation",methods=['post'])
def UpdateReservation():
    return HOTEL_RES_POST_UPDATE_UpdateReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_UpdateFixedRateReservation",methods=['POST'])
def insertfixedrate():
    return HOTEL_RES_POST_INSERT_UpdateFixedRateReservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryFixedRateReservation",methods=['POST'])
def Queryfixedrate():
    return HOTEL_RES_GET_SELECT_QueryFixedRateReservation(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateFixedRateReservation",methods=['POST'])
def updatefixedrate():
    return HOTEL_RES_POST_UPDATE_UpdateFixedRateReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_WaitlistReservation",methods=['POST'])
def waitlistreservation():
    return HOTEL_RES_POST_INSERT_WaitlistReservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryWaitlistReservation",methods=['POST'])
def queryWaitlistReservation():
    return HOTEL_RES_GET_SELECT_QueryWaitlistReservation(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateWaitlistReservation",methods=['POST'])
def updatewaitlistreservation():
    return HOTEL_RES_POST_UPDATE_UpdateWaitlistReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_UpdateAlertReservation",methods=['POST'])
def alertreservation():
    return HOTEL_RES_POST_INSERT_UpdateAlertReservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryAlertReservation",methods=['POST'])
def queryalert():
    return HOTEL_RES_GET_SELECT_QueryAlertReservation(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateReservationAlert",methods=['POST'])
def updatealert():
    return HOTEL_RES_POST_UPDATE_UpdateReservationAlert(request)
@app.route("/Hotel_RES_POST_Select_QueryReservationActivitylog",methods=['POST'])
def queryreservationactivitylog():
    return Hotel_RES_POST_Select_QueryReservationActivitylog(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation",methods=['POST'])
def updatefixedcharges():
    return HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryFixedChargesReservation",methods=['POST'])
def queryfixedcharges():
    return HOTEL_RES_GET_SELECT_QueryFixedChargesReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_UpdateDeposit",methods=['POST'])
def insertdeposit():
    return HOTEL_RES_POST_INSERT_UpdateDeposit(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateDeposit",methods=['POST'])
def updatedeposit():
    return HOTEL_RES_POST_UPDATE_UpdateDeposit(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryDepositrule",methods=['POST'])
def querydepositrule():
    return HOTEL_RES_GET_SELECT_QueryDepositrule(request)
@app.route("/HOTEL_RES_GET_SELECT_RoomUnassign",methods=['POST'])
def roomunassign():
    return HOTEL_RES_GET_SELECT_RoomUnassign(request)
@app.route("/Hotel_RES_Post_Insert_UpdateGuestPrivileges",methods=['POST'])
def GuestPrivileges():
    return Hotel_RES_Post_Insert_UpdateGuestPrivileges(request)
@app.route("/Hotel_RES_Post_Update_UpdateGuestPrivileges",methods=['POST'])
def UpdateGuestPrivileges():
    return Hotel_RES_Post_Update_UpdateGuestPrivileges(request)
@app.route("/Hotel_RES_Get_Select_QueryGuestPrivileges",methods=['POST'])
def SelectGuestPrivileges():
    return Hotel_RES_Get_Select_QueryGuestPrivileges(request)
@app.route("/Hotel_RES_Post_Insert_UpdateGuestTraces",methods=['POST'])
def GuestTraces():
    return Hotel_RES_Post_Insert_UpdateGuestTraces(request)
@app.route("/Hotel_RES_Post_Update_UpdateGuestTraces",methods=['POST'])
def UpdateGuestTraces():
    return Hotel_RES_Post_Update_UpdateGuestTraces(request)
@app.route("/Hotel_RES_Get_Select_QueryGuestTraces",methods=['GET'])
def SelectGuestTraces():
    return Hotel_RES_Get_Select_QueryGuestTraces()
@app.route("/HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation",methods=['POST'])
def UpdateFixedChargesReservation():
    return HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation(request)
@app.route('/Hotel_Res_Post_Select_Queryreservation',methods=['POST'])
def Queryreservation():
   return hotel_res_post_select_queryreservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryReservationSearch",methods=['GET'])
def QueryReservationSearchVALY():
    return QueryReservationSearch()
@app.route("/HOTEL_RES_POST_SELECT_QueryHistoryReservation",methods=['POST'])
def QueryHistoryReservationVALUE():
    return QueryHistoryReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_CancelReservation",methods=['POST'])
def HOTEL_RES_POST_INSERT_CancelReservationvalue():
    return HOTEL_RES_POST_INSERT_CancelReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_ReinstateReservation",methods=['POST'])
def HOTEL_RES_POST_INSERT_ReinstateReservationvalue():
    return HOTEL_RES_POST_INSERT_ReinstateReservation(request)
@app.route("/HOTEL_RES_POST_SELECT_QueryArrivalFromToReservation",methods=['POST'])
def HOTEL_RES_POST_SELECT_QueryArrivalFromToReservationVAL():
    return HOTEL_RES_POST_SELECT_QueryArrivalFromToReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_WaitlistReason",methods=['POST'])
def HOTEL_RES_POST_INSERT_WaitlistReasonval():
    return HOTEL_RES_POST_INSERT_WaitlistReason(request)
@app.route("/HOTEL_RES_POST_INSERT_AcceptWaitlistReservation",methods=['POST'])
def HOTEL_RES_POST_INSERT_AcceptWaitlistReservationval():
    return HOTEL_RES_POST_INSERT_AcceptWaitlistReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_ReservationCreditcard",methods=['POST'])
def HOTEL_RES_POST_INSERT_ReservationCreditcardval():
    return HOTEL_RES_POST_INSERT_ReservationCreditcard(request)
@app.route("/Hotel_RES_Post_Update_UpdateReservationCreditcard",methods=['POST'])
def Hotel_RES_Post_Update_UpdateReservationCreditcardval():
    return Hotel_RES_Post_Update_UpdateReservationCreditcard(request)
@app.route("/Hotel_RES_Get_Select_QueryReservationCreditcard",methods=['POST'])
def Hotel_RES_Get_Select_QueryReservationCreditcardval():
    return Hotel_RES_Get_Select_QueryReservationCreditcard(request)
@app.route("/HOTEL_RES_POST_DELETE_DeleteReservation",methods=['POST'])
def HOTEL_RES_POST_DELETE_DeleteReservationval():
    return HOTEL_RES_POST_DELETE_DeleteReservation(request)
@app.route("/Hotel_RES_Post_Update_TracesResloved",methods=['POST'])
def Hotel_RES_Post_Update_TracesReslovedvs():
    return Hotel_RES_Post_Update_TracesResloved(request)
@app.route("/HOTEL_RES_POST_UPDATE_RoomMove",methods=['POST'])
def HOTEL_RES_POST_UPDATE_RoomMoveval():
    return HOTEL_RES_POST_UPDATE_RoomMove(request)
@app.route("/Hotel_RES_POST_Delete_DeleteReservationCreditcard",methods=['POST'])
def Hotel_RES_POST_Delete_DeleteReservationCreditcardva():
    return Hotel_RES_POST_Delete_DeleteReservationCreditcard(request)
@app.route("/HOTEL_RES_POST_SELECT_QueryDeposit",methods=['POST'])
def HOTEL_RES_POST_SELECT_QueryDepositva():
    return HOTEL_RES_POST_SELECT_QueryDeposit(request)


@app.route("/Hotel_RES_POST_INSERT_RestypeInsert",methods=['POST'])
def Hotel_RES_POST_INSERT_RestypeInsertvalue():
    return Hotel_RES_POST_INSERT_RestypeInsert(request)
@app.route("/Hotel_RES_POST_INSERT_Alertarea",methods=['POST'])
def Hotel_RES_POST_INSERT_Alertareava():
    return Hotel_RES_POST_INSERT_Alertarea(request)
@app.route("/Hotel_RES_POST_INSERT_Alertcode",methods=['POST'])
def Hotel_RES_POST_INSERT_Alertcodeva():
    return Hotel_RES_POST_INSERT_Alertcode(request)
@app.route("/Hotel_RES_POST_INSERT_Origin",methods=['POST'])
def Hotel_RES_POST_INSERT_Originva():
    return Hotel_RES_POST_INSERT_Origin(request)
@app.route("/Hotel_RES_POST_INSERT_Source",methods=['POST'])
def Hotel_RES_POST_INSERT_Sourceva():
    return Hotel_RES_POST_INSERT_Source(request)
@app.route("/Hotel_RES_POST_INSERT_Payment",methods=['POST'])
def Hotel_RES_POST_INSERT_Paymentvalue():
   return Hotel_RES_POST_INSERT_Payment(request)
@app.route("/Hotel_RES_POST_INSERT_Market",methods=['POST'])
def Hotel_RES_POST_INSERT_Marketvalue():
   return Hotel_RES_POST_INSERT_Market(request)
@app.route("/Hotel_RES_POST_INSERT_Department",methods=['POST'])
def Hotel_RES_POST_INSERT_Departmentvalt():
   return Hotel_RES_POST_INSERT_Department(request)
@app.route("/Hotel_RES_POST_INSERT_Transaction_code",methods=['POST'])
def Hotel_RES_POST_INSERT_Transaction_codevalue():
   return Hotel_RES_POST_INSERT_Transaction_code(request)
@app.route("/Hotel_RES_POST_INSERT_Depositrule",methods=['POST'])
def Hotel_RES_POST_INSERT_Depositruleva():
   return Hotel_RES_POST_INSERT_Depositrule(request)
@app.route("/Hotel_RES_POST_INSERT_CancelReason",methods=['POST'])
def Hotel_RES_POST_INSERT_CancelReasonval():
   return Hotel_RES_POST_INSERT_CancelReason(request)
@app.route("/Hotel_RES_POST_INSERT_Cardtype",methods=['POST'])
def Hotel_RES_POST_INSERT_Cardtypeva():
   return Hotel_RES_POST_INSERT_Cardtype(request)
@app.route("/Hotel_RES_POST_INSERT_Waitlist_reason",methods=['POST'])
def Hotel_RES_POST_INSERT_Waitlist_reasonva():
   return Hotel_RES_POST_INSERT_Waitlist_reason(request)

@app.route("/Hotel_RES_GET_SELECT_Restype",methods=['GET'])
def Hotel_RES_GET_SELECT_Restypesfs():
    return Hotel_RES_GET_SELECT_Restype()
@app.route("/Hotel_RES_GET_SELECT_Alertarea",methods=['GET'])
def Hotel_RES_GET_SELECT_Alertareavalue():
    return Hotel_RES_GET_SELECT_Alertarea()
@app.route("/Hotel_RES_GET_SELECT_Alertcode",methods=['GET'])
def Hotel_RES_GET_SELECT_Alertcodevalue():
    return Hotel_RES_GET_SELECT_Alertcode()
@app.route("/Hotel_RES_GET_SELECT_Origin",methods=['GET'])
def Hotel_RES_GET_SELECT_Originvalue():
    return Hotel_RES_GET_SELECT_Origin()
@app.route("/Hotel_RES_GET_SELECT_Source",methods=['GET'])
def Hotel_RES_GET_SELECT_Sourceva():
    return Hotel_RES_GET_SELECT_Source()
@app.route("/Hotel_RES_GET_SELECT_Payment",methods=['GET'])
def Hotel_RES_GET_SELECT_Paymentvalur():
   return Hotel_RES_GET_SELECT_Payment()
@app.route("/Hotel_RES_GET_SELECT_Market",methods=['GET'])
def Hotel_RES_GET_SELECT_Marketgads():
   return Hotel_RES_GET_SELECT_Market()
@app.route("/Hotel_RES_GET_SELECT_Department",methods=['GET'])
def Hotel_RES_GET_SELECT_Departmentvalue():
   return Hotel_RES_GET_SELECT_Department()
@app.route("/Hotel_RES_GET_SELECT_Transaction_code",methods=['GET'])
def Hotel_RES_GET_SELECT_Transaction_codevalue():
   return Hotel_RES_GET_SELECT_Transaction_code()
@app.route("/Hotel_RES_GET_SELECT_depositrule",methods=['GET'])
def Hotel_RES_GET_SELECT_depositruledasd():
   return Hotel_RES_GET_SELECT_depositrule()
@app.route("/Hotel_RES_GET_SELECT_CancelReason",methods=['GET'])
def Hotel_RES_GET_SELECT_CancelReasonvalue():
   return Hotel_RES_GET_SELECT_CancelReason()
@app.route("/Hotel_RES_GET_SELECT_Cardtype",methods=['GET'])
def Hotel_RES_GET_SELECT_Cardtypeva():
   return Hotel_RES_GET_SELECT_Cardtype()
@app.route("/Hotel_RES_GET_SELECT_Waitlist_reason",methods=['GET'])
def Hotel_RES_GET_SELECT_Waitlist_reasonva():
   return Hotel_RES_GET_SELECT_Waitlist_reason()
@app.route("/Hotel_RES_GET_SELECT_Privileges",methods=['GET','POST'])
def Hotel_RES_GET_SELECT_Privileges_all():
  return Hotel_RES_GET_SELECT_Privileges()

@app.route("/ProfileFutureReservation",methods=['POST'])
def futurereservation():
    return ProfileFutureReservation(request)
@app.route("/Reservationdonutchart",methods=['GET'])
def Reservationdonutchart_all():
    return Reservationdonutchart()
@app.route("/HOTEL_RES_POST_SELECT_RateQuery",methods=['POST'])
def HOTEL_RES_POST_SELECT_RateQuery_all():
    return HOTEL_RES_POST_SELECT_RateQuery(request)
@app.route("/HOTEL_RES_POST_INSERT_AttachAcompanyingGuest",methods=['POST'])
def HOTEL_RES_POST_INSERT_AttachAcompanyingGuest_all():
    return HOTEL_RES_POST_INSERT_AttachAcompanyingGuest(request)
@app.route("/HOTEL_RES_POST_INSERT_DetachAcompanyingGuest",methods=['POST'])
def HOTEL_RES_POST_INSERT_DetachAcompanyingGuest_all():
    return HOTEL_RES_POST_INSERT_DetachAcompanyingGuest(request)
@app.route("/HOTEL_RES_POST_SELECT_QueryAccompanyingGuest",methods=['POST'])
def HOTEL_RES_POST_SELECT_QueryAccompanyingGuest_all():
    return HOTEL_RES_POST_SELECT_QueryAccompanyingGuest(request)


@app.route("/Hotel_RES_Post_SELECT_QueryTransactioncodeCode",methods=['POST'])
def Hotel_RES_Post_SELECT_QueryTransactioncodeCode_all():
    return Hotel_RES_Post_SELECT_QueryTransactioncodeCode(request)
@app.route("/Hotel_RES_Post_SELECT_SelectFixedCharges",methods=['POST'])
def Hotel_RES_Post_SELECT_SelectFixedCharges_all():
    return Hotel_RES_Post_SELECT_SelectFixedCharges(request)
@app.route("/HOTEL_RES_POST_SELECT_QueryFixedRateReservation",methods=['POST'])
def HOTEL_RES_POST_SELECT_QueryFixedRateReservation_all():
    return HOTEL_RES_POST_SELECT_QueryFixedRateReservation(request)
@app.route("/Hotel_RES_Post_Delete_RemoveTraces",methods=['POST'])
def Hotel_RES_Post_Delete_RemoveTraces_all():
    return Hotel_RES_Post_Delete_RemoveTraces(request)
@app.route("/Hotel_RES_Post_Select_PropertyCalendar",methods=['POST'])
def Hotel_RES_Post_Select_PropertyCalendar_all():
    return Hotel_RES_Post_Select_PropertyCalendar(request)
@app.route("/HOTEL_RES_POST_SELECT_QueryRateInfo",methods=['POST'])
def HOTEL_RES_POST_SELECT_QueryRateInfo_all():
    return HOTEL_RES_POST_SELECT_QueryRateInfo(request)
@app.route("/HOTEL_RES_POST_SELECT_QueryPackageOptions",methods=['POST'])
def HOTEL_RES_POST_SELECT_QueryPackageOptions_all():
    return HOTEL_RES_POST_SELECT_QueryPackageOptions(request)
@app.route("/HOTEL_RES_POST_Insert_RoomRouting",methods=['POST'])
def HOTEL_RES_POST_Insert_RoomRouting_all():
    return HOTEL_RES_POST_Insert_RoomRouting(request)
@app.route("/Hotel_RES_Get_Select_QueryRoomRouting",methods=['POST'])
def Hotel_RES_Get_Select_QueryRoomRouting_all():
    return Hotel_RES_Get_Select_QueryRoomRouting(request)
@app.route("/HOTEL_RES_POST_select_Paticularreservation",methods=['POST'])
def HOTEL_RES_POST_select_Paticularreservation_all():
    return HOTEL_RES_POST_select_Paticularreservation(request)
#</----------------------------/>
#<---------------frontdesk route----------------------->
@app.route("/HOTEL_FD_POST_INSERT_UpdateQueueRreservation",methods=['POST'])
def insertqueue():
    return HOTEL_FD_POST_INSERT_UpdateQueueRreservation(request)
@app.route("/HOTEL_FD_POST_SELECT_QueryQueueReservation",methods=['POST'])
def queryqueue():
    return HOTEL_FD_POST_SELECT_QueryQueueReservation(request)
@app.route("/HOTEL_FD_POST_UPDATE_RoomAssign",methods=['POST'])
def roomassignGUETS():
    return HOTEL_FD_POST_UPDATE_RoomAssign(request)
@app.route("/HOTEL_FD_POST_UPDATE_CheckinGuestArrivals",methods=['POST'])
def guestarrivals():
    return HOTEL_FD_POST_UPDATE_CheckinGuestArrivals(request)
@app.route("/HOTEL_FD_GET_SELECT_QueryTracesActivityLog",methods=['GET'])
def HOTEL_FD_GET_SELECT_QueryTracesActivityLogva():
    return HOTEL_FD_GET_SELECT_QueryTracesActivityLog()
@app.route("/HOTEL_FD_POST_SELECT_QueryRoomAssignment",methods=['GET'])
def HOTEL_FD_POST_SELECT_QueryRoomAssignmentva():
    return HOTEL_FD_POST_SELECT_QueryRoomAssignment()

@app.route("/Hotel_RES_POST_INSERT_Privileges",methods=['POST'])
def Hotel_RES_POST_INSERT_Privileges_one():
  return Hotel_RES_POST_INSERT_Privileges(request)

@app.route("/HOTEL_FD_GET_SELECT_QueryNotes",methods=['POST'])
def HOTEL_FD_GET_SELECT_QueryNotes_all():
  return HOTEL_FD_GET_SELECT_QueryNotes(request)
@app.route("/HOTEL_FD_GET_SELECT_Querypreference",methods=['POST'])
def HOTEL_FD_GET_SELECT_Querypreference_al():
  return HOTEL_FD_GET_SELECT_Querypreference(request)
#<--------------------------------------------->
#<----------------------Room maangement route------------------->
@app.route('/Hotel_Rm_Post_Insert_Updateroomlist',methods=['POST'])
def Updateroomlist():
   return hotel_rm_post_insert_updateroomlist(request)
@app.route('/Hotel_Rm_Post_Update_Updateroomstatus',methods=['POST'])
def Updateroomstatus():
   return Hotel_Rm_Post_Update_Updateroomstatus(request)
@app.route("/Hotel_Rm_Post_Select_QueryRoomList",methods=['POST','GET'])
def QueryRoomList():
   return hotel_rm_post_select_queryroomlist(request)
@app.route("/Hotel_Rm_Post_Select_QueryRoomStatistics",methods=['POST'])
def QueryRoomStatistics():
   return hotel_rm_post_select_queryroomstatistics(request)
@app.route('/Hotel_Rm_Post_Insert_Updateroomcondition',methods=['POST'])
def Updateroomcondition():
   return hotel_rm_post_insert_updateroomcondition(request)
@app.route("/Hotel_Rm_Post_Select_QueryRoomCondition",methods=['POST','GET'])
def QueryRoomCondition():
   return hotel_rm_post_select_queryroomcondition(request)
@app.route("/Hotel_Rm_Post_Delete_RoomCondition",methods=['POST'])
def deleteRoomCondition():
   return hotel_rm_post_delete_roomcondition(request)
@app.route("/hotel_rm_post_update_updateroomdiscrepancies",methods=['POST'])
def updateroomdiscrepancies():
   return hotel_rm_post_update_updateroomdiscrepancies(request)
@app.route('/Hotel_Rm_Post_Select_QueryRoomDiscrepancies',methods=['POST','GET'])
def QueryRoomDiscrepancies ():
   return hotel_rm_post_select_queryroomdiscrepancies(request)
@app.route('/Hotel_Rm_Post_Insert_UpdateGuestServiceStatus',methods=['POST'])
def UpdateGuestServiceStatus():
   return hotel_rm_post_insert_updateguestservicestatus(request)
@app.route('/Hotel_Rm_Post_Select_QueryGuestServiceStatus',methods=['POST'])
def QueryGuestServiceStatus():
   return hotel_rm_post_select_queryguestservicestatus(request)
@app.route('/Hotel_Rm_Post_Insert_Updateoutoforderservice',methods=['POST'])
def Insertoutoforderservice():
   return hotel_rm_post_insert_updateoutoforderservice(request)
@app.route('/Hotel_Rm_Post_Select_Queryoutoforderservice',methods=['POST'])
def Queryoutoforderservice ():
   return hotel_rm_post_select_queryoutoforderservice(request)
@app.route('/Hotel_Rm_Post_Insert_Updateroommaintenance',methods=['POST'])
def Insertroommaintenance ():
   return hotel_rm_post_insert_updateroommaintenance(request)
@app.route('/Hotel_Rm_Post_Update_ResolveRoomMaintenance',methods=['POST'])
def ResolveRoomMaintenance ():
   return hotel_rm_post_update_resolveroommaintenance(request)
@app.route('/Hotel_Rm_Post_Select_Queryroommaintenance',methods=['POST'])
def Queryroommaintenance():
   return hotel_rm_post_select_queryroommaintenance(request)
@app.route('/Hotel_Rm_Post_Delete_Deleteoutoforderservice',methods=['POST'])
def Deleteoutoforderservice():
   return hotel_rm_post_delete_deleteoutoforderservice(request)
@app.route('/Hotel_Rm_Post_Delete_DeleteRoomMaintenance',methods=['POST'])
def DeleteRoomMaintenance():
   return hotel_rm_post_delete_deleteroommaintenance(request)
@app.route('/hotel_rm_post_update_updateroomcondition',methods=['POST'])
def hotel_rm_post_update_updateroomconditiond():
   return hotel_rm_post_update_updateroomcondition(request)
@app.route('/Hotel_Rm_Post_Update_Updateoutoforderservices',methods=['POST'])
def Updateoutoforderservice():
   return hotel_rm_post_update_updateoutoforderservice(request)


#Pending room management--------------------------

@app.route('/Hotel_RM_Post_SELECT_OccupancyGraph',methods=['POST'])
def Hotel_RM_Post_SELECT_OccupancyGraph_all():
   return Hotel_RM_Post_SELECT_OccupancyGraph(request)
@app.route('/hotel_rm_post_Update_guestservicestatus',methods=['POST'])
def hotel_rm_post_Update_guestservicestatus_all():
   return hotel_rm_post_Update_guestservicestatus(request)
@app.route('/hotel_rm_post_select_OutoforderRoomsonly',methods=['POST'])
def hotel_rm_post_select_OutoforderRoomsonly_all():
   return hotel_rm_post_select_OutoforderRoomsonly(request)
@app.route('/hotel_rm_post_Select_Turndown_management',methods=['POST'])
def hotel_rm_post_Select_Turndown_management_all():
   return hotel_rm_post_Select_Turndown_management(request)
@app.route('/Hotel_RM_Post_SELECT_FacilityForecast',methods=['POST'])
def Hotel_RM_Post_SELECT_FacilityForecast_all():
   return Hotel_RM_Post_SELECT_FacilityForecast(request)
@app.route('/hotel_rm_post_update_Turndown_management',methods=['POST'])
def hotel_rm_post_update_Turndown_management_all():
   return hotel_rm_post_update_Turndown_management(request)
@app.route('/hotel_rm_post_select_Dropdown_Turndown_management',methods=['POST'])
def hotel_rm_post_select_Dropdown_Turndown_management_all():
   return hotel_rm_post_select_Dropdown_Turndown_management(request)


#deopdown
@app.route("/Select_RoomStatus",methods=['POST'])
def Select_RoomStatus():
  return select_roomstatus()
@app.route("/Select_Class",methods=['POST'])
def Select_Class():
  return select_class()
@app.route("/Select_Condition",methods=['POST'])
def Select_Condition():
  return select_condition()
@app.route("/Select_Hkstatus_Code",methods=['POST'])
def Select_Hkstatus_Code():
  return select_hkstatus_code()
@app.route("/Select_Room_Type",methods=['POST'])
def Select_Room_Type():
  return select_room_type()
@app.route("/Select_Room_No",methods=['POST'])
def Select_Room_No():
  return select_room_no()
@app.route("/Select_Discription",methods=['POST'])
def Select_Discription():
  return select_discription()
@app.route("/Select_Servicestatus_Code",methods=['POST'])
def Select_Servicestatus_Code():
  return select_servicestatus_code()
@app.route("/Select_Turndownstatus",methods=['POST'])
def Select_Turndownstatus():
  return select_turndownstatus()
@app.route("/select_room_service_status",methods=['POST'])
def select_room_service_statusvalue():
  return select_room_service_status()
@app.route("/select_mainteanance_reason",methods=['POST'])
def select_mainteanance_reasonva():
  return select_mainteanance_reason()
@app.route("/select_floor",methods=['POST'])
def select_floorcs():
  return select_floor()
#insert
@app.route("/Insert_Roomstatus",methods=['POST'])
def Insert_Roomstatus():
  return insert_roomstatus(request)
@app.route("/Insert_Class",methods=['POST'])
def Insert_Class():
  return insert_class(request)
@app.route("/Insert_Condition",methods=['POST'])
def Insert_Condition():
  return insert_condition(request)
@app.route("/insert_hkstatus_code",methods=['POST'])
def insert_hkstatus_code_value():
  return insert_hkstatus_code(request)
@app.route("/insert_room_type",methods=['POST'])
def insert_room_type_value():
  return insert_room_type(request)
@app.route("/insert_room_no",methods=['POST'])
def insert_room_no_value():
  return insert_room_no(request)
@app.route("/insert_room_discription",methods=['POST'])
def insert_room_discription_value():
  return insert_room_discription(request)
@app.route("/insert_servicestatus_code",methods=['POST'])
def insert_servicestatus_codevalue():
  return insert_servicestatus_code(request)
@app.route("/insert_turndownstatus",methods=['POST'])
def insert_turndownstatus_value():
  return insert_turndownstatus(request)
@app.route("/insert_room_service_status",methods=['POST'])
def insert_room_service_statusva():
  return insert_room_service_status(request)
@app.route("/insert_mainteanance_reason",methods=['POST'])
def insert_mainteanance_reasonva():
  return insert_mainteanance_reason(request)
@app.route("/insert_floor",methods=['POST'])
def insert_floordd():
  return insert_floor(request)
#<--------------------------------------------------------->
#<--------------amazonlex-------------------------->
@app.route('/AMAZON_RESERVATION_LAMBDA_LEX',methods=['GET'])
def amazonlex():
   return AMAZON_RESERVATION_LAMBDA_LEX(request)
@app.route('/amazon_insert',methods=['POST'])
def amazon_insert_all():
   return amazon_insert(request)
@app.route('/CheckConfirmation',methods=['POST'])
def CheckConfirmation_all():
   return CheckConfirmation(request)
@app.route('/checkinguest',methods=['POST'])
def checkinguest_all():
   return checkinguest(request)
@app.route('/Checkroom',methods=['POST'])
def Checkroom_all():
   return Checkroom(request)
@app.route('/sendemailkeyfault',methods=['POST'])
def sendemailkeyfault_all():
   return callexternalapi(request)
#<----------------------------------------------->
#<----------------------Revenue management------------------>
@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_INSERT_RATECATEGORY",methods=['POST'])
def revenuerate():
    return ratecategory(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_INSERT_RATECODE",methods=['POST'])
def ratecodee():
    return ratecode(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_INSERT_MARKET",methods=['POST'])
def markete():
    return market(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_INSERT_SOURCE",methods=['POST'])
def source():
    return sourcetab(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_INSERT_CURRENCY",methods=['POST'])
def currency():
    return crrencytab(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_SELECT_RATECATEGORY",methods=['POST'])
def revenuerateselect():
    return rateselect(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_SELECT_RATECODE",methods=['POST'])
def ratecodesel():
    return ratecodeselect(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_SELECT_MARKET_SELECT",methods=['POST'])
def marksel():
    return marketselect(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_SELECT_MARKET_SOURCE_SELECT",methods=['POST'])
def sourcesel():
    return sourceselect(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_SELECT_MARKET_CURRENCY_SELECT",methods=['POST'])
def currencysource():
    return currencyselect(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_POST_INSERT_NEGOTIATED",methods=['POST'])
def negotiatedd():
    return negotiated(request)

@app.route("/HOTEL_CAH_POST_INSERT_UPDATERATECODESETUP",methods=['POST'])
def ratecodesetupcash():
    return HOTEL_CAH_POST_INSERT_UPDATERATECODESETUP(request)

@app.route("/HOTEL_REM_POST_INSERT_RATE_DETAILS",methods=['POST'])
def ratedet():
    return ratedetailss(request)
@app.route("/HOTEL_REM_POST_INSERT_UpdateRatecodeSetup",methods=['POST'])
def HOTEL_REM_POST_INSERT_UpdateRatecodeSetupsas():
    return HOTEL_REM_POST_INSERT_UpdateRatecodeSetup(request)
@app.route("/HOTEL_REM_POST_SELECT_QueryRatecode",methods=['POST'])
def HOTEL_REM_POST_SELECT_QueryRatecodeds():
  return HOTEL_REM_POST_SELECT_QueryRatecode(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_SELECT_Roomtype",methods=['POST'])
def select_roomtype_reveneue():
  return room_types(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_SELECT_Packages",methods=['POST'])
def select_packages_reveneue():
  return packages_revenue(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_SELECT_Seasoncode",methods=['POST'])
def select_season_reveneue():
  return season_code_revenue(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_Insert_season_code_revenue",methods=['POST'])
def Insert_season_code_revenue_all():
  return Insert_season_code_revenue(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_SELECT_Ratecodes",methods=['POST'])
def select_ratecodes_reveneue():
  return HOTEL_REM_POST_SELECT_Ratecode(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_SELECT_Negotiated_Rate",methods=['POST','GET'])
def select_negotiated_rate_reveneue():
  return HOTEL_REM_POST_SELECT_Negotiated_Rate(request)

@app.route("/HOTEL_REVENUE_MANAGEMENT_DELETE_Negotiated_Rate",methods=['POST'])
def delete_negotiated_rate_reveneue():
  return Delete_Negotiated_Rate(request)

@app.route("/HOTEL_REM_POST_UPDATE_UpdateRatecodeSetup",methods=['POST'])
def UPDATE_UpdateRatecodeSetup():
  return HOTEL_REM_POST_UPDATE_UpdateRatecodeSetup(request)

@app.route("/HOTEL_REM_POST_SELECT_UpdateRatecodeSetup",methods=['POST'])
def SELECT_UpdateRatecodeSetup():
  return HOTEL_REM_POST_SELECT_UpdateRatecodeSetup(request)

@app.route("/HOTEL_REM_POST_UPDATE_Negotiated_Rate",methods=['POST'])
def UPDATE_Negotiated_Rate():
  return HOTEL_REM_POST_UPDATE_Negotiated_Rate(request)

@app.route("/HOTEL_REM_POST_SELECT_SelectRatesetupAll",methods=['POST','GET'])
def SELECT_SelectRatesetupAll():
  return HOTEL_REM_POST_SELECT_SelectRatesetupAll(request)

@app.route("/HOTEL_REM_POST_UPDATE_RATE_DETAILS",methods=['POST'])
def UPDATE_RATE_DETAILS():
  return HOTEL_REM_POST_UPDATE_RATE_DETAILS(request)

@app.route("/Delete_Rate_code",methods=['POST'])
def Delete_Ratecode():
  return Delete_Rate_code(request)

@app.route("/Delete_Rate_details",methods=['POST'])
def Delete_Ratedetails():
  return Delete_Rate_details(request)

#<---------------------------------------CASHIER-------------------------------------------------->

@app.route("/HOTEL_CAH_POST_INSERT_UPDATEGUESTBILLING",methods=['POST'])
def insertguestbillingcash():
  return HOTEL_CAH_POST_INSERT_UPDATEGUESTBILLING(request)

@app.route("/HOTEL_CAH_POST_UPDATE_UPDATEGUESTBILLING",methods=['POST'])
def updateguestbillingcharges():
   return HOTEL_CAH_POST_UPDATE_UPDATEGUESTBILLING(request)

@app.route("/HOTEL_CAH_POST_SELECT_QUERYGUESTBILLING",methods=['POST'])
def querybilling():
  return HOTEL_CAH_POST_SELECT_QUERYGUESTBILLING(request)


@app.route("/HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENT",methods=['POST'])
def updatepostingcash():
    return HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENT(request)

@app.route("/HOTEL_CAH_POST_POSTING_HISTORY_LOG",methods=['POST'])
def historylog():
    return HOTEL_CAH_POST_POSTING_HISTORY_LOG(request)

@app.route("/HOTEL_CAH_POST_FOLIO_HISTORY",methods=['POST','GET'])
def folio():
    return HOTEL_CAH_POST_FOLIO_HISTORY(request)

@app.route("/HOTEL_CAH_POST_UPDATE_TransfertoAnotherWindow",methods=['POST'])
def transfer():
    return HOTEL_CAH_POST_UPDATE_TransfertoAnotherWindow(request)

@app.route("/HOTEL_CASH_BILLING_CODE_INSERT",methods=['POST'])
def billing():
    return HOTEL_CASH_BILLING_CODE_INSERT(request)

@app.route("/HOTEL_CASH_BILLING_CODE_SELECT",methods=['POST'])
def billingcode():
    return HOTEL_CASH_BILLING_CODE_SELECT(request)

@app.route("/HOTEL_CASH_INSERT_BILLING_CURRENCY",methods=['POST'])
def billingcurrency():
    return HOTEL_CASH_INSERT_BILLING_CURRENCY(request)

@app.route("/HOTEL_CASH_SELECT_POSTING_WINDOW",methods=['POST'])
def postingwindow():
    return HOTEL_CASH_SELECT_POSTING_WINDOW(request)

@app.route("/HOTEL_CASH_RESERVATION_BALANCE",methods=['POST'])
def reservation_balance():
     return HOTEL_CASH_RESERVATION_BALANCE(request)

@app.route("/HOTEL_CASH_RESERVATION_STATUS",methods=['POST'])
def reservationstatus():
    return HOTEL_CASH_RESERVATION_STATUS(request)

@app.route("/HOTEL_CAH_POST_CASH_CHECK_OUT",methods=['POST'])
def cashcheckout():
    return HOTEL_CAH_POST_CASH_CHECK_OUT(request)

@app.route("/HOTEL_CAH_POST_POSTING_PAYMENT",methods=['POST'])
def posting():
    return HOTEL_CAH_POST_POSTING_PAYMENT(request)

@app.route("/HOTEL_CAH_POST_POSTING_PAYMENT_INSERT",methods=['POST'])
def paymentinsert():
    return HOTEL_CAH_POST_POSTING_PAYMENT_INSERT(request)

@app.route("/HOTEL_CAH_POST_POSTING_CHANGES_HISTORY_LOG",methods=['POST'])
def changeshistory():
    return HOTEL_CAH_POST_POSTING_CHANGES_HISTORY_LOG(request)

@app.route("/HOTEL_CAH_POST_POSTING_ORIGINAL_HISTOR_LOG",methods=['POST'])
def originalhistory():
    return HOTEL_CAH_POST_POSTING_ORIGINAL_HISTOR_LOG(request)

@app.route("/HOTEL_CAH_POST_UPDATE_TransfertoAnotherRoom",methods=['POST'])
def anotherroom():
    return HOTEL_CAH_POST_UPDATE_TransfertoAnotherRoom(request)

@app.route("/HOTEL_CAH_POST_SELECT_QUERYINHOUSERECORD",methods=['POST','GET'])
def QUERYINHOUSERECORD():
    return HOTEL_CAH_POST_SELECT_QUERYINHOUSERECORD(request)

@app.route("/HOTEL_CASH_PAYMENT_CODE_SELECT",methods=['POST','GET'])
def PAYMENT_CODE_SELECT():
    return HOTEL_CASH_PAYMENT_CODE_SELECT(request)

@app.route("/HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENTCHECKOUT",methods=['POST'])
def UPDATEPOSTINGPAYMENTCHECKOUT():
    return HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENTCHECKOUT(request)



#<-------------------------Business Block------------------------------->

@app.route("/HOTEL_BBL_POST_INSERT_BusinessBlock",methods=['POST'])
def inquiryprocess():
    return HOTEL_BBL_POST_INSERT_BusinessBlock(request)


@app.route("/HOTEL_BBL_POST_UPDATE_Business_Block_Update",methods=['POST'])
def businessupdate():
    return HOTEL_BBL_POST_UPDATE_Business_Block_Update(request)


@app.route("/HOTEL_BBL_POST_INSERT_Business_Block_Notes",methods=['POST'])
def blocknotes():
    return HOTEL_BBL_POST_INSERT_Business_Block_Notes(request)


@app.route("/HOTEL_BBL_POST_INSERT_GroupCancel",methods=['POST'])
def groupcancel():
    return HOTEL_BBL_POST_INSERT_GroupCancel(request)


@app.route("/HOTEL_BBL_GET_SELECT_BusinessBlockSearch",methods=['GET'])
def blocksearch():
    return HOTEL_BBL_GET_SELECT_BusinessBlockSearch()


@app.route("/HOTEL_BBL_POST_SELECT_Business_Block_activitylog",methods=['POST'])
def activitylog():
    return HOTEL_BBL_POST_SELECT_Business_Block_activitylog(request)

@app.route("/HOTEL_BBL_POST_SELECT_QueryGroupCancel",methods=['POST'])
def querygroupcancel():
    return HOTEL_BBL_POST_SELECT_QueryGroupCancel(request)


@app.route("/HOTEL_BBL_POST_INSERT_BusinessBlockDefinite",methods = ['POST'])
def businessblockdefinite():
    return HOTEL_BBL_POST_INSERT_BusinessBlockDefinite(request)
@app.route("/HOTEL_BBL_POST_INSERT_GroupReservations",methods = ['POST'])
def groupreservation():
    return HOTEL_BBL_POST_INSERT_GroupReservation(request)
@app.route("/HOTEL_BBL_POST_SELECT_QueryInquiryGrid",methods = ['POST'])
def inquirygrid():
    return HOTEL_BBL_POST_SELECT_QueryInquiryGrid(request)

@app.route("/HOTEL_BBL_POST_UPDATE_BusinessBlockStatus",methods= ['POST'])
def blockstatus():
   return HOTEL_BBL_POST_UPDATE_BusinessBlockStatus(request)
@app.route("/HOTEL_BBL_POST_UPDATE_BusinessBlockDefinite",methods = ['POST'])
def UpdateBusinessBlockDefinite():
   return HOTEL_BBL_POST_UPDATE_BusinessBlockDefinite(request)

@app.route("/HOTEL_BBL_POST_INSERT_Grid",methods=['POST'])
def grid():
   return HOTEL_BBL_POST_INSERT_Grid(request)
@app.route("/HOTEL_BBL_POST_UPDATE_UpdateGrid",methods=['POST'])
def Updategrid():
   return HOTEL_BBL_POST_UPDATE_UpdateGrid(request)

@app.route("/HOTEL_BBL_POST_SELECT_QueryGrid",methods=['POST'])
def querygrid():
   return HOTEL_BBL_POST_SELECT_QueryGrid(request)

@app.route("/HOTEL_BBL_POST_INSERT_CalculateRoomRevenue",methods=['POST'])
def Revenue():
   return HOTEL_BBL_POST_INSERT_CalculateRoomRevenue(request)

@app.route("/HOTEL_BBL_POST_SELECT_QueryRoomRevenue",methods=['POST'])
def QueryRevenue():
   return HOTEL_BBL_POST_SELECT_QueryRoomRevenue(request)

@app.route("/HOTEL_BBL_POST_INSERT_PayMasterReservation",methods=['POST'])
def paymaster():
   return HOTEL_BBL_POST_INSERT_PayMasterReservation(request)
@app.route("/HOTEL_BBL_POST_SELECT_QueryGroupReservation",methods=['POST'])
def HOTEL_BBL_POST_SELECT_QueryGroupReservationdff():
   return HOTEL_BBL_POST_SELECT_QueryGroupReservation(request)
@app.route("/HOTEL_BBL_POST_SELECT_QueryPayMasterReservation",methods=['POST'])
def HOTEL_BBL_POST_SELECT_QueryPayMasterReservationder():
   return HOTEL_BBL_POST_SELECT_QueryPayMasterReservation(request)
@app.route("/HOTEL_BBL_POST_SELECT_EditBusinessBlockSearch",methods=['POST'])
def EditBusinessBlockSearch():
   return HOTEL_BBL_POST_SELECT_EditBusinessBlockSearch(request)

@app.route("/HOTEL_BBL_POST_SELECT_SelectRoomingList_Roomtype",methods=['POST'])
def SelectRoomingList_Roomtype():
   return HOTEL_BBL_POST_SELECT_SelectRoomingList_Roomtype(request)

@app.route("/HOTEL_BBL_POST_UPDATE_UpdateRoomingList_Roomtype",methods=['POST'])
def UpdateRoomingList_Roomtype():
   return HOTEL_BBL_POST_UPDATE_UpdateRoomingList_Roomtype(request)

@app.route("/HOTEL_BBL_POST_SELECT_SelectRoomtype",methods=['POST'])
def specific_SelectRoomtype():
   return HOTEL_BBL_POST_SELECT_SelectRoomtype(request)

@app.route("/HOTEL_BBL_POST_SELECT_gridservice",methods=['POST'])
def HOTEL_BBL_POST_SELECT_gridservicevv():
   return HOTEL_BBL_POST_SELECT_gridservice(request)
@app.route("/HOTEL_BBL_POST_SELECT_Business_Block_Notes",methods=['POST'])
def HOTEL_BBL_POST_SELECT_Business_Block_Notes_all():
   return HOTEL_BBL_POST_SELECT_Business_Block_Notes(request)

#<------------------Buiness Block dropdown---------->
@app.route("/HOTEL_BBL_GET_SELECT_BusinessBlockStatus",methods=['GET'])
def blockstatusert():
   return HOTEL_BBL_GET_SELECT_BusinessBlockStatus()

@app.route("/HOTEL_BBL_GET_SELECT_InventoryContrtol",methods=['GET'])
def INVENTORY():
   return HOTEL_BBL_GET_SELECT_InventoryContrtol()


@app.route("/HOTEL_BBL_GET_SELECT_MeetingSpaceType",methods=['GET'])
def meeting_space():
   return HOTEL_BBL_GET_SELECT_MeetingSpaceType()
@app.route("/HOTEL_BBL_GET_SELECT_Block_Type",methods=['GET'])
def HOTEL_BBL_GET_SELECT_Block_Typebgg():
   return HOTEL_BBL_GET_SELECT_Block_Type()

@app.route("/HOTEL_BBL_POST_INSERT_BusinessBlockStatus",methods=['POST'])
def HOTEL_BBL_POST_INSERT_BusinessBlockStatus_all():
   return HOTEL_BBL_POST_INSERT_BusinessBlockStatus(request)
@app.route("/HOTEL_BBL_POST_INSERT_InventoryContrtol",methods=['POST'])
def inventory():
   return HOTEL_BBL_POST_INSERT_InventoryContrtol(request)
@app.route("/HOTEL_BBL_POST_INSERT_MeetingSpaceType",methods=['POST'])
def HOTEL_BBL_POST_INSERT_MeetingSpaceType_all():
   return HOTEL_BBL_POST_INSERT_MeetingSpaceType(request)
@app.route("/HOTEL_BBL_POST_INSERT_Block_Type",methods=['POST'])
def HOTEL_BBL_POST_INSERT_Block_Type_all():
   return HOTEL_BBL_POST_INSERT_Block_Type(request)


#<-------------------Packages--------------------------------------->

@app.route("/HOTEL_PAC_POST_INSERT_Forecastgroup",methods=['POST'])
def INSERT_Forecastgroup():
   return HOTEL_PAC_POST_INSERT_Forecastgroup(request)

@app.route("/HOTEL_PAC_POST_INSERT_Transactioncode",methods=['POST'])
def INSERT_Transactioncode():
   return HOTEL_PAC_POST_INSERT_Transactioncode(request)

@app.route("/HOTEL_PAC_POST_INSERT_Attributes",methods=['POST'])
def INSERT_Attributes():
   return HOTEL_PAC_POST_INSERT_Attributes(request)

@app.route("/HOTEL_PAC_POST_INSERT_Postingrhythm",methods=['POST'])
def INSERT_Postingrhythm():
   return HOTEL_PAC_POST_INSERT_Postingrhythm(request)

@app.route("/HOTEL_PAC_POST_INSERT_Calculaterule",methods=['POST'])
def INSERT_Calculaterule():
   return HOTEL_PAC_POST_INSERT_Calculaterule(request)

@app.route("/HOTEL_PAC_POST_INSERT_Iteminventory",methods=['POST'])
def INSERT_Iteminventory():
   return HOTEL_PAC_POST_INSERT_Iteminventory(request)

@app.route("/HOTEL_PAC_POST_SELECT_Forecastgroup",methods=['POST'])
def SELECT_Forecastgroup():
   return HOTEL_PAC_POST_SELECT_Forecastgroup(request)

@app.route("/HOTEL_PAC_POST_SELECT_Transactioncode",methods=['POST'])
def SELECT_Transactioncode():
   return HOTEL_PAC_POST_SELECT_Transactioncode(request)

@app.route("/HOTEL_PAC_POST_SELECT_Postingrhythm",methods=['POST'])
def SELECT_Postingrhythm():
   return HOTEL_PAC_POST_SELECT_Postingrhythm(request)

@app.route("/HOTEL_PAC_POST_SELECT_Calculaterule",methods=['POST'])
def SELECT_Calculaterule():
   return HOTEL_PAC_POST_SELECT_Calculaterule(request)

@app.route("/HOTEL_PAC_POST_SELECT_Iteminventory",methods=['POST'])
def SELECT_Iteminventory():
   return HOTEL_PAC_POST_SELECT_Iteminventory(request)

@app.route("/HOTEL_PAC_POST_INSERT_Packages",methods=['POST'])
def INSERT_Packages():
   return HOTEL_PAC_POST_INSERT_Packages(request)

@app.route("/HOTEL_PAC_POST_INSERT_Packagesdetails",methods=['POST'])
def INSERT_Packagesdetails():
   return HOTEL_PAC_POST_INSERT_Packagesdetails(request)

@app.route("/HOTEL_PAC_POST_UPDATE_Packages",methods=['POST'])
def UPDATE_Packages():
   return HOTEL_PAC_POST_UPDATE_Packages(request)

@app.route("/HOTEL_PAC_POST_SELECT_Packages",methods=['POST'])
def SELECT_Packages():
   return HOTEL_PAC_POST_SELECT_Packages(request)

@app.route("/HOTEL_PAC_POST_SELECT_Packages_All",methods=['POST'])
def SELECT_Packages_All():
   return HOTEL_PAC_POST_SELECT_Packages_All(request)

@app.route("/HOTEL_PAC_POST_DELETE_Package",methods=['POST'])
def DELETE_Package():
   return HOTEL_PAC_POST_DELETE_Package(request)

@app.route("/HOTEL_PAC_POST_DELETE_Packagedetails",methods=['POST'])
def DELETE_Packagedetails():
   return HOTEL_PAC_POST_DELETE_Packagedetails(request)
@app.route("/HOTEL_PAC_POST_SELECT_PackagesTrasnactioncode",methods=['POST'])
def HOTEL_PAC_POST_SELECT_PackagesTrasnactioncode_alls():
   return HOTEL_PAC_POST_SELECT_PackagesTrasnactioncode(request)

#dddddddd
#<------------------------------------------------------------------>
#PMS Report*************************************************
@app.route("/GetReservationReport",methods=['POST'])
def GetReservationReport_all():
   return GetReservationReport(request)
@app.route("/GetFrontDeskReport",methods=['POST'])
def GetFrontDeskReport_all():
   return GetFrontDeskReport(request)
@app.route("/GetBusinessBlock",methods=['POST'])
def GetBusinessBlock_all():
   return GetBusinessBlock(request)
@app.route("/GetProfileReport",methods=['POST'])
def GetProfileReport_all():
   return GetProfileReport(request)
@app.route("/GetRoomHousekeeping",methods=['POST'])
def GetRoomHousekeeping_all():
   return GetRoomHousekeeping(request)
@app.route("/GetFrontofficestatus",methods=['POST'])
def GetFrontofficestatus_all():
   return GetFrontofficestatus(request)
@app.route("/GetRoomcondition",methods=['POST'])
def conditionroom_all():
   return GetRoomconditionall(request)
@app.route("/GetRoomDiscrepencies",methods=['POST'])
def RoomDiscrepencies_all():
   return GetRoomDiscrepencies(request)
@app.route("/GetGuestServiceStatus",methods=['POST'])
def GetGuestServiceStatus_all():
   return GetGuestServiceStatus(request)
@app.route("/GetZerobalanceaccount",methods=['POST'])
def GetZerobalanceaccount_all():
   return GetZerobalanceaccount(request)
@app.route("/GetReservationNoshowreport",methods=['POST'])
def GetReservationNoshowreport_all():
   return GetReservationNoshowreport(request)
@app.route("/HistoryBooking",methods=['POST'])
def HistoryBooking_all():
   return HistoryBooking()
@app.route("/futurebooking",methods=['POST'])
def futurebooking_all():
   return futurebooking()
@app.route("/Cashiergettotalamount",methods=['POST'])
def Cashiergettotalamount_all():
   return Cashiergettotalamount(request)

@app.route("/RoomHistory",methods=['POST','GET'])
def RoomHistory_all():
   return RoomHistory(request)
#<------------------------account receviable----------------------------->
#<--------------------Account Receivable------------------------------>
@app.route("/HOTEL_AR_POST_INSERT_AccountSetup",methods=['POST'])
def INSERT_AccountSetup():
   return HOTEL_AR_POST_INSERT_AccountSetup(request)

@app.route("/HOTEL_AR_POST_UPDATE_AccountSetup",methods=['POST'])
def UPDATE_AccountSetup():
   return HOTEL_AR_POST_UPDATE_AccountSetup(request)

@app.route("/HOTEL_AR_POST_SELECT_AccountSetup",methods=['POST'])
def SELECT_AccountSetup():
   return HOTEL_AR_POST_SELECT_AccountSetup(request)

@app.route("/HOTEL_AR_POST_DELETE_AccountSetup",methods=['POST'])
def DELETE_AccountSetup():
   return HOTEL_AR_POST_DELETE_AccountSetup(request)

@app.route("/HOTEL_AR_POST_INSERT_ArNotes",methods=['POST'])
def INSERT_ArNotes():
   return HOTEL_AR_POST_INSERT_ArNotes(request)

@app.route("/HOTEL_AR_POST_UPDATE_ArNotes",methods=['POST'])
def UPDATE_ArNotes():
   return HOTEL_AR_POST_UPDATE_ArNotes(request)

@app.route("/HOTEL_AR_POST_SELECT_ArNotes",methods=['POST'])
def SELECT_ArNotes():
   return HOTEL_AR_POST_SELECT_ArNotes(request)

@app.route("/HOTEL_AR_POST_DELETE_ArNotes",methods=['POST'])
def DELETE_ArNotes():
   return HOTEL_AR_POST_DELETE_ArNotes(request)

@app.route("/HOTEL_AR_POST_SELECT_ArPostHistory",methods=['POST'])
def SELECT_ArPostHistory():
   return HOTEL_AR_POST_SELECT_ArPostHistory(request)

@app.route("/HOTEL_AR_POST_INSERT_AccountTraces",methods=['POST'])
def INSERT_AccountTraces():
   return HOTEL_AR_POST_INSERT_AccountTraces(request)

@app.route("/HOTEL_AR_POST_UPDATE_AccountTraces",methods=['POST'])
def UPDATE_AccountTraces():
   return HOTEL_AR_POST_UPDATE_AccountTraces(request)

@app.route("/HOTEL_AR_POST_SELECT_AccountTraces",methods=['POST'])
def SELECT_AccountTraces():
   return HOTEL_AR_POST_SELECT_AccountTraces(request)

@app.route("/HOTEL_AR_POST_DELETE_AccountTraces",methods=['POST'])
def DELETE_AccountTraces():
   return HOTEL_AR_POST_DELETE_AccountTraces(request)

@app.route("/HOTEL_AR_POST_INSERT_AccountInvoice",methods=['POST'])
def INSERT_AccountInvoice():
   return HOTEL_AR_POST_INSERT_AccountInvoice(request)
@app.route("/HOTEL_AR_POST_SELECT_AccountInvoice",methods=['POST'])
def SELECT_AccountInvoice():
   return HOTEL_AR_POST_SELECT_AccountInvoice(request)
@app.route("/HOTEL_AR_POST_DELETE_AccountInvoice",methods=['POST'])
def DELETE_AccountInvoice():
   return HOTEL_AR_POST_DELETE_AccountInvoice(request)

@app.route("/HOTEL_AR_POST_INSERT_Billingpost",methods=['POST'])
def HOTEL_AR_POST_INSERT_Billingpost_all():
   return HOTEL_AR_POST_INSERT_Billingpost(request)
@app.route("/HOTEL_AR_POST_SELECT_Billingpost",methods=['POST'])
def HOTEL_AR_POST_SELECT_Billingpost_ALL():
   return HOTEL_AR_POST_SELECT_Billingpost(request)
@app.route("/HOTEL_AR_POST_UPDATE_AdjustBillingpost",methods=['POST'])
def HOTEL_AR_POST_UPDATE_AdjustBillingpost_all():
   return HOTEL_AR_POST_UPDATE_AdjustBillingpost(request)
@app.route("/HOTEL_AR_POST_INSERT_Billingpayment",methods=['POST'])
def HOTEL_AR_POST_INSERT_Billingpayment_all():
   return HOTEL_AR_POST_INSERT_Billingpayment(request)
@app.route("/HOTEL_AR_POST_SELECT_AccountPostHistory",methods=['POST'])
def HOTEL_AR_POST_SELECT_AccountPostHistory_all():
   return HOTEL_AR_POST_SELECT_AccountPostHistory(request)

@app.route("/HOTEL_AR_POST_SELECT_AccountPayHistory",methods=['POST'])
def HOTEL_AR_POST_SELECT_AccountPayHistory_all():
   return HOTEL_AR_POST_SELECT_AccountPayHistory(request)


@app.route("/HOTEL_AR_POST_SELECT_ApplyPaymentSelectiviely",methods=['POST'])
def HOTEL_AR_POST_SELECT_ApplyPaymentSelectiviely_all():
   return HOTEL_AR_POST_SELECT_ApplyPaymentSelectiviely(request)
@app.route("/HOTEL_AR_POST_INSERT_UNApplyPayment",methods=['POST'])
def HOTEL_AR_POST_SELECT_UNApplyPayment_all():
   return HOTEL_AR_POST_INSERT_UNApplyPayment(request)
@app.route("/HOTEL_AR_POST_SELECT_ReversePayment",methods=['POST'])
def HOTEL_AR_POST_SELECT_ReversePayment_all():
   return HOTEL_AR_POST_SELECT_ReversePayment(request)
@app.route("/HOTEL_AR_POST_SELECT_UnappyPayment",methods=['POST'])
def HOTEL_AR_POST_SELECT_UnappyPayment_all():
   return HOTEL_AR_POST_SELECT_UnappyPayment(request)
@app.route("/HOTEL_AR_POST_INSERT_CompressInvoice",methods=['POST'])
def HOTEL_AR_POST_INSERT_CompressInvoice_all():
   return HOTEL_AR_POST_INSERT_CompressInvoice(request)
@app.route("/HOTEL_AR_POST_DELETE_UnCompressInvoice",methods=['POST'])
def HOTEL_AR_POST_DELETE_UnCompressInvoice_all():
   return HOTEL_AR_POST_DELETE_UnCompressInvoice(request)

@app.route("/HOTEL_AR_POST_SELECT_YearViewAmount",methods=['POST'])
def HOTEL_AR_POST_SELECT_YearViewAmount_all():
   return HOTEL_AR_POST_SELECT_YearViewAmount(request)

@app.route("/HOTEL_AR_POST_INSERT_Account_typeDropdown",methods=['POST'])
def HOTEL_AR_POST_INSERT_Account_typeDropdown_all():
   return HOTEL_AR_POST_INSERT_Account_typeDropdown(request)

@app.route("/HOTEL_AR_POST_SELECT_Account_typeDropdown",methods=['POST'])
def HOTEL_AR_POST_SELECT_Account_typeDropdown_all():
   return HOTEL_AR_POST_SELECT_Account_typeDropdown(request)

@app.route("/HOTEL_AR_POST_INSERT_REASONDropdown",methods=['POST'])
def HOTEL_AR_POST_INSERT_REASONDropdown_all():
   return HOTEL_AR_POST_INSERT_REASONDropdown(request)

@app.route("/HOTEL_AR_POST_SELECT_REASONDropdown",methods=['POST'])
def HOTEL_AR_POST_SELECT_REASONDropdown_all():
   return HOTEL_AR_POST_SELECT_REASONDropdown(request)
@app.route("/HOTEL_AR_POST_INSERT_ARTransfer",methods=['POST'])
def HOTEL_AR_POST_INSERT_ARTransfer_all():
   return HOTEL_AR_POST_INSERT_ARTransfer(request)

@app.route("/HOTEL_AR_POST_SELECT_InvoicePaymentDropdown",methods=['POST'])
def HOTEL_AR_POST_SELECT_InvoicePaymentDropdown_all():
   return HOTEL_AR_POST_SELECT_InvoicePaymentDropdown(request)
@app.route("/HOTEL_AR_POST_INSERT_InvoicePaymentDropdown",methods=['POST'])
def HOTEL_AR_POST_INSERT_InvoicePaymentDropdown_all():
   return HOTEL_AR_POST_INSERT_InvoicePaymentDropdown(request)
@app.route("/HOTEL_AR_POST_SELECT_AccountTypeDropdown",methods=['POST'])
def HOTEL_AR_POST_SELECT_AccountTypeDropdown_all():
   return HOTEL_AR_POST_SELECT_AccountTypeDropdown(request)



#<---------------------------------End of day route-------------------->
@app.route("/Hotel_END_OF_Day_POST_countrycheck",methods=['POST'])
def Hotel_END_OF_Day_POST_countrycheck_all():
   return Hotel_END_OF_Day_POST_countrycheck(request)
@app.route("/Hotel_END_OF_Day_POST_Departure_Not_Checkedout",methods=['POST'])
def Hotel_END_OF_Day_POST_Departure_Not_Checkedout_all():
   return Hotel_END_OF_Day_POST_Departure_Not_Checkedout(request)
@app.route("/Hotel_END_OF_Day_POST_Roll_Business_date",methods=['POST'])
def Hotel_END_OF_Day_POST_Roll_Business_date_all():
   return Hotel_END_OF_Day_POST_Roll_Business_date(request)
@app.route("/Hotel_END_OF_Day_POST_Posting_Rooms_charges",methods=['POST'])
def Hotel_END_OF_Day_POST_Posting_Rooms_charges_all():
   return Hotel_END_OF_Day_POST_Posting_Rooms_charges(request)
@app.route("/Hotel_END_OF_Day_POST_Run_Additional_procedures",methods=['POST'])
def Run_Additional_procedures():
   return Hotel_END_OF_Day_POST_Run_Additional_procedures(request)
@app.route("/Hotel_END_OF_Day_POST_print_final_report",methods=['POST'])
def Hotel_END_OF_Day_POST_print_final_report_all():
   return Hotel_END_OF_Day_POST_print_final_report(request)

#<--------------------------PMS Merge module webservice
@app.route("/Hotel_PMS_Select_GetTodayRoomAvailabilityArrival",methods=['POST'])
def Hotel_PMS_Select_GetTodayRoomAvailabilityArrival_all():
   return Hotel_PMS_Select_GetTodayRoomAvailabilityArrival(request)

@app.route("/Hotel_PMS_cancel_DepositRuleReservation",methods=['POST'])
def Hotel_PMS_cancel_DepositRuleReservation_all():
   return Hotel_PMS_cancel_DepositRuleReservation(request)


@app.route("/Hotel_PMS_Select_BlockFollowupDecisiondate",methods=['POST'])
def Hotel_PMS_Select_BlockFollowupDecisiondate_all():
   return Hotel_PMS_Select_BlockFollowupDecisiondate(request)
@app.route("/Hotel_PMS_Select_Blockcutoffdatecutoffdays",methods=['POST'])
def Hotel_PMS_Select_Blockcutoffdatecutoffdays_all():
   return Hotel_PMS_Select_Blockcutoffdatecutoffdays(request)

@app.route("/Hotel_PMS_Select_DepositDueDate",methods=['POST'])
def Hotel_PMS_Select_DepositDueDate_all():
   return Hotel_PMS_Select_DepositDueDate(request)

@app.route("/Hotel_PMS_Select_Roominglistdue_date",methods=['POST'])
def Hotel_PMS_Select_Roominglistdue_date_ALL():
   return Hotel_PMS_Select_Roominglistdue_date(request)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="192.168.99.1",port=5000)

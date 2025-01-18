package com.bizconnectivity.gino;

public class ConstantWS {

    // Web Service Namespace & SOAP Action
    public static final String NAMESPACE = "http://tempuri.org/";
    public static final String SOAP_ACTION = "http://tempuri.org/";

    // BCPL Development Server
    public static final String URL = "http://192.168.2.91/ginows/MobileWebService.asmx";

    // Web Service Name

    // User
    public static final String WS_CREATE_USER = "Mobile_CreateMember";
    public static final String WS_RETRIEVE_USER = "Mobile_GetMemberByEmail";
    public static final String WS_UPDATE_USER = "Mobile_UpdateMember";
    public static final String WS_UPDATE_USER_PASSWORD = "Mobile_UpdateMemberPassword";
    public static final String WS_UPDATE_USER_PHOTO = "Mobile_UploadMemberPhoto";
    public static final String WS_CHECK_USER = "Mobile_MemberEmailAvailability";
    public static final String WS_CHECK_USER_LOGIN = "Mobile_CheckMemberLogin";

    // User Deal
    public static final String WS_CREATE_USER_DEAL = "Mobile_CreateMemberDeal";
    public static final String WS_UPDATE_USER_DEAL = "Mobile_UpdateMemberDeal";
    public static final String WS_RETRIEVE_AVAILABLE_DEAL = "Mobile_GetMemberAvailableDeal";
    public static final String WS_RETRIEVE_HISTORY_DEAL = "Mobile_GetMemberHistoryDeal";
    public static final String WS_RETRIEVE_USER_DEAL_DETAIL = "Mobile_GetMemberDealDetail";

    // Deal
    public static final String WS_RETRIEVE_DEAL = "Mobile_GetDeal";
    public static final String WS_RETRIEVE_DEAL_BY_CATEGORY = "Mobile_GetDealByCategory";
    public static final String WS_RETRIEVE_DEAL_BY_CREATED_DATE = "Mobile_GetDealOrderByCreatedDate";
    public static final String WS_RETRIEVE_DEAL_BY_NO_OF_VIEW = "Mobile_GetDealOrderByNoOfView";
    public static final String WS_RETRIEVE_USER_DEAL = "Mobile_GetUserDeal";
    public static final String WS_RETRIEVE_USER_DEAL_BY_CATEGORY = "Mobile_GetUserDealByCategory";
    public static final String WS_RETRIEVE_USER_DEAL_BY_CREATED_DATE = "Mobile_GetUserDealOrderByCreatedDate";
    public static final String WS_RETRIEVE_USER_DEAL_BY_NO_OF_VIEW = "Mobile_GetUserDealOrderByNoOfView";
    public static final String WS_RETRIEVE_DEAL_BY_ID = "Mobile_GetDealById";
    public static final String WS_UPDATE_DEAL_NO_OF_VIEW = "Mobile_UpdateDealNoOfView";
    public static final String WS_RETRIEVE_SEARCH_DEAL = "Mobile_SearchDeal";

    // Deal Category
    public static final String WS_RETRIEVE_DEAL_CATEGORY = "Mobile_GetDealCategory";
    public static final String WS_RETRIEVE_DEAL_CATEGORY_BY_ID = "Mobile_GetDealCategoryById";

    // Event
    public static final String WS_RETRIEVE_EVENT = "Mobile_GetNearbyEvent";
    public static final String WS_RETRIEVE_EVENT_BY_ID = "Mobile_GetEventById";
    public static final String WS_RETRIEVE_EVENT_FILTER = "Mobile_NearbyEventFilter";

    // Merchant
    public static final String WS_RETRIEVE_MERCHANTS = "Mobile_GetMerchants";
    public static final String WS_RETRIEVE_MERCHANT_BY_ID = "Mobile_GetMerchantById";

    // Dismissed Deal
    public static final String WS_CREATE_DISMISSED_DEAL = "Mobile_CreateMemberDismissedDeal";
    public static final String WS_RETRIEVE_DISMISSED_DEAL = "Mobile_GetMemberDismissedDeal";
    public static final String WS_DELETE_DISMISSED_DEAL = "Mobile_DeleteMemberDismissedDeal";

    // Favourite Deal
    public static final String WS_CREATE_FAVOURITE_DEAL = "Mobile_CreateMemberFavouriteDeal";
    public static final String WS_RETRIEVE_FAVOURITE_DEAL = "Mobile_GetMemberFavouriteDeal";
    public static final String WS_DELETE_FAVOURITE_DEAL = "Mobile_DeleteMemberFavouriteDeal";

    // Favourite Event
    public static final String WS_CREATE_FAVOURITE_EVENT = "Mobile_CreateMemberFavouriteEvent";
    public static final String WS_RETRIEVE_FAVOURITE_EVENT = "Mobile_GetMemberFavouriteEvent";
    public static final String WS_DELETE_FAVOURITE_EVENT = "Mobile_DeleteMemberFavouriteEvent";
    public static final String WS_CHECK_FAVOURITE_EVENT = "Mobile_CheckMemberFavouriteEvent";
}

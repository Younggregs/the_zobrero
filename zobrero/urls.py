from django.conf.urls import url
from rest_framework.authtoken import views as drf_views

from . import views
app_name = 'zobrero'

urlpatterns = [
    #auth/
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),

    #zobrero/
    url(r'^$',views.index, name = 'index'),

    #zobrero/accounts
    url(r'^accounts/$',views.AddAccount.as_view(), name = 'add-account'),

    #zobrero/signin
    url(r'^signin/$',views.SignIn.as_view(), name = 'sign-in'),

    #zobrero/600
    url(r'^accounts/(?P<account_id>[0-9]+)/$',views.AccountDetail.as_view(), name = 'account-detail'),

    #zobrero/talent_category
    url(r'^talent_category/$',views.TalentCategory.as_view(), name = 'talent-category'),

    #zobrero/all_talents
    url(r'^all_talents/(?P<category_id>[0-9]+)/$',views.AllTalent.as_view(), name = 'all-talent'),

    #zobrero/add_employee
    url(r'^add_employee/$',views.AddEmployeeAccount.as_view(), name = 'add-employee-account'),

    #zobrero/top_rated
    url(r'^top_rated/$',views.TopRated.as_view(), name = 'top-rated'),

    #zobrero/search
    url(r'^search/$',views.Search.as_view(), name = 'search'),

    #zobrero/isloggedin
    url(r'^isloggedin/$',views.IsLoggedIn.as_view(), name = 'is-logged-in'),

    #zobrero/is_myaccount
    url(r'^is_myprofile/(?P<profile_id>[0-9]+)$',views.IsMyProfile.as_view(), name = 'is-my-profile'),

    #zobrero/ismyaccount/profile_id
    url(r'^myaccount_id/$',views.MyAccountID.as_view(), name = 'my-account-id'),

    #zobrero/getaccount
    url(r'^getaccount/$',views.GetAccount.as_view(), name = 'get-account'),

    #zobrero/recent_activity
    url(r'^recent_activity/$',views.RecentActivityView.as_view(), name = 'recent-activity-view'),

    #zobrero/top_rated
    url(r'^top_rated/$',views.TopRatedView.as_view(), name = 'top-rated-view'),

    #zobrero/whats_new
    url(r'^whats_new/$',views.WhatsNewView.as_view(), name = 'whats-new-view'),
   
    #zobrero/reset_dp
    url(r'^reset_dp/$',views.ResetDP.as_view(), name = 'reset-dp'),

    #zobrero/signin
    url(r'^update_password/$',views.UpdatePassword.as_view(), name = 'update-password'),

    #zobrero/signin
    url(r'^reset_phone/$',views.ResetPhone.as_view(), name = 'reset-phone'),

    #zobrero/chatclients
    url(r'^chatclients/$',views.ChatClients.as_view(), name = 'chat-clients'),

    #zobrero/haggleclients
    url(r'^new_chat/(?P<client_id>[0-9]+)/$',views.NewChat.as_view(), name = 'new-chat'),

    #zobrero/messenger
    url(r'^messenger/(?P<client_id>[0-9]+)/$',views.MessengerView.as_view(), name = 'messenger'),

    #zobrero/messenger
    url(r'^unread_messages/$',views.UnreadMessages.as_view(), name = 'unread-messages'),

    #zobrero/send_message
    url(r'^send_message/(?P<client_id>[0-9]+)/$',views.SendMessage.as_view(), name = 'send-message'),

    #zobrero/status
    url(r'^status/$',views.StatusView.as_view(), name = 'status-view'),

    #zobrero/getaccount_name
    url(r'^getaccount_name/(?P<account_id>[0-9]+)/$',views.GetAccountName.as_view(), name = 'get-account-name'),

    #zobrero/appointment
    url(r'^appointment/(?P<client_id>[0-9]+)/$',views.AppointmentView.as_view(), name = 'appointment-view'),


]

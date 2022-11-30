from django.urls import path
from appsmartip.views import *

urlpatterns = [
     path('', home, name="Home"), 
     path('admin_db/', admin_db, name='AdminDB'),
     path('admin_db/office', admin_db_office, name='AdminDbOffice'),
     path('admin_db/devtype', admin_db_dev_type, name='AdminDbDevType'),
     path('admin_db/status', admin_db_status, name='AdminDbStatus'),
     path('admin_db/tech', admin_db_tech, name='AdminDbTech'),
     path('admin_db/user', admin_db_user, name='AdminDbUser'),
     path('dev_manager', dev_manager, name='DevManager'),
     path('pending', pending, name='Pending'),
     path('search', search, name='Search'),
     path('search/dev', search_dev, name='SearchDisp'),
     path('search/dev/result', search_dev_result, name='SearchDevResult'),
     path('search/ip', search_ip, name='SearchIp'),
     path('search/result/details', search_result_detail, name='SearchResultDetail'),
     path('search/office', search_office, name='SearchOffice'),
     path('search/office/result', search_office_result, name='SearchOfficeResult'),
     path('search/user', search_user, name='SearchUser'),
     path('search/user/result', search_user_result, name='SearchUserResult'),

]

from django.urls import path
from appsmartip.views import *

urlpatterns = [
     # Home
     path('', home, name="Home"), 
     
     # Registration
     path('register/', register, name='Register'),
     
     # Db Admin Menu    
     path('admin_db/', admin_db, name='AdminDB'),
     
     # Database Admin - Locations   
     path('admin_db/location/', admin_db_location, name='AdminDbLocation'),

     # Database Admin - Ediffices   
     path('admin_db/office/', admin_db_ediffice, name='AdminDbEdiffice'),

     # Database Admin - offices   
     path('admin_db/office/', admin_db_office, name='AdminDbOffice'),
     
     #Database Admin - Devices Type
     path('admin_db/devType/', admin_db_dev_type, name='AdminDbDevType'),

     #Database Admin - Devices Brand
     path('admin_db/devBrand/', admin_db_dev_type, name='AdminDbDevBrand'),

     #Database Admin - Ip´
     path('admin_db/ip/', search_ip, name='AdminDbIp'),

     #Database Admin - Internet Access
     
     #CRUD  Database Admin - Devices Type
     path('admin_db/dev_type/add/', add_dev_type, name='AddDevType'),
     
     #CRUD Database Admin - Model 
     path('admin_db/dev_model/', dev_models, name='AdminDbDevModel'),
     path('admin_db/dev_model/add/', add_dev_model, name='AddDevModel'),
     path('admin_db/dev_model/list/', list_dev_model, name='AdminDevModelList'),
     path('admin_db/dev_model/edit/<id>/', edit_dev_model, name='EditDevModel'),
     path('dev_model_delete/<id>/', delete_dev_model, name='DeleteDevModel'),

     path('admin_db/status/', admin_db_status, name='AdminDbStatus'),
     path('admin_db/tech/', admin_db_tech, name='AdminDbTech'),
     path('admin_db/user/', admin_db_user, name='AdminDbUser'),
     path('dev_manager/', dev_manager, name='DevManager'),
     path('dev_manager/filtred/', dev_manager_filtred_result, name='DevResult'),
     path('dev_manager/detail/', device_details, name='DevDetails'),
     path('pending/', pending, name='Pending'),
     path('search/', search, name='Search'),
     path('search/dev/', search_dev, name='SearchDevice'),
     path('search/dev/result/', search_dev_result, name='SearchDevResult'),
     path('search/ip/', search_ip, name='SearchIp'),
     path('search/result/details/', search_result_detail, name='SearchResultDetail'),
     path('search/office/', search_office, name='SearchOffice'),
     path('search/office/result/', search_office_result, name='SearchOfficeResult'),
     path('search/user/', search_user, name='SearchUser'),
     path('search/user/result/', search_user_result, name='SearchUserResult'),

]

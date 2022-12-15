from django.urls import path, include
from appsmartip.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('model', ModelViewset)


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
     
     #! Database Admin - Devices Type
     path('admin_db/devType/', admin_db_dev_type, name='AdminDbDevType'),
     # path('admin_db/devType/<id>/', admin_db_dev_type_edit, name='AdminDbDevTypeEdit'),
     path('admin_db/devType/<id>/', admin_db_dev_type, name='AdminDbDevType'),

     #Database Admin - Devices Brand
     path('admin_db/devBrand/', admin_db_dev_type, name='AdminDbDevBrand'),

     #Database Admin - Ip´
     path('admin_db/ip/', search_ip, name='AdminDbIp'),
     path('admin_db/ip/add', add_ip, name='IpAdd'),

     #Database Admin - Internet Access
     path('admin_db/internet/', search_ip, name='AdminDbInternet'),
     
     #CRUD Database Admin - Model 
     path('admin_db/dev_model/', list_dev_model, name='AdminDbDevModel'),
     path('admin_db/dev_model/add/', add_dev_model, name='AddDevModel'),
     path('admin_db/dev_model/edit/<id>/', edit_dev_model, name='EditDevModel'),
     path('dev_model_delete/<id>/', delete_dev_model, name='DeleteDevModel'),
     
     #django rest model url
     path('api/', include(router.urls)),

     path('admin_db/status/', admin_db_status, name='AdminDbStatus'),
     path('admin_db/tech/', admin_db_tech, name='AdminDbTech'),
     path('admin_db/user/', admin_db_user, name='AdminDbUser'),
     
     #device manager
     path('dev_manager/', dev_manager, name='DevManager'),
     path('dev_manager/add', dev_manager_add, name='DevAdd'),
     path('dev_manager/details/<id>/', dev_manager_details, name='DevDetails'),
     path('dev_manager/edit/<id>/', dev_manager_edit, name='DevEdit'),
     path('dev_manager_delete/<id>/', dev_manager_delete, name='DevDelete'),


     path('pendings/', pending, name='Pending'),
     path('pendings/pendings_list/', pending_list, name='PendingList'),
     path('pendings/pendings_edit/<id>', pending_edit, name='PendingEdit'),

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

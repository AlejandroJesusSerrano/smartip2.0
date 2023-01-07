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

     # Database Admin - offices   
     path('admin_db/office/', admin_db_offices, name='Offices'),
     path('admin_db/office/add/', offices_add, name='OfficesAdd'),
     path('admin_db/office/edit/<id>/', offices_edit, name='OfficeEdit')
     path('office_delete/<id>/', office_delete, name='OfficeDelete'),
     
     #* Database Admin - Devices Type
     path('admin_db/devType/', admin_db_dev_type, name='AdminDbDevType'),
     path('admin_db/devType/add', add_dev_type, name='AddType'),
     path('admin_db/devType/update/<id>/',edit_dev_type, name ='UpdateType'),
     path('delete_dev_type/<id>/', delete_dev_type, name='DeleteType'),

     #* Database Admin - Devices Brand
     path('admin_db/brand/', admin_db_brand, name='AdminDbDevBrand'),
     path('admin_db/brand/add/', add_brand, name='AddBrand'),
     path('admin_db/brand/edit/<id>/',edit_brand, name ='UpdateBrand'),
     path('delete_brand/<id>/', delete_brand, name='DeleteBrand'),

     #* Database Admin - Model 
     path('admin_db/dev_model/', list_dev_model, name='AdminDbDevModel'),
     path('admin_db/dev_model/add/', add_dev_model, name='AddDevModel'),
     path('admin_db/dev_model/edit/<id>/', edit_dev_model, name='EditDevModel'),
     path('dev_model_delete/<id>/', delete_dev_model, name='DeleteDevModel'),
     
     #* Database Admin - Internet Access Type
     path('admin_db/i_access/', list_access, name='InAccessList'),
     path('admin_db/i_access/add/', add_access, name='InternetAdd'),
     path('admin_db/i_access/edit/<id>/', edit_access, name='InternetEdit'),
     path('i_access_delete/<id>/', delete_access, name='InternetDelete'),
     
     #* Database Admin - Ip´
     path('admin_db/ip', list_ips, name="IpHome"),
     path('admin_db/ip/add', add_ip, name='IpAdd'),
     path('admin_db/ip/edit/<id>', edit_ip, name='IpEdit'),
     path('ip_delete/<id>/', delete_ip, name='ipDelete'),

     #* Database Admin - Locations   
     path('admin_db/location/', admin_db_location, name='Location'),
     path('admin_db/location/add/', location_add, name='LocationAdd'),
     path('admin_db/location/edit/<id>/', location_edit, name='LocationEdit'),
     path('delete_location/<id>/', location_delete, name='LocationDelete'),

     #* Database Admin - Ediffices   
     path('admin_db/ediffices/', admin_db_ediffice, name='Ediffices'),   
     path('admin_db/ediffices/add/', ediffice_add, name='EdifficesAdd'),     
     path('admin_db/ediffices/edit/<id>/', ediffice_edit, name='EdifficesEdit'),  
     path('delete_ediffice/<id>/', ediffice_delete, name='EdifficesDelete'),
     
     #* django rest model url
     path('api/', include(router.urls)),

     path('admin_db/status/', admin_db_status, name='AdminDbStatus'),
     path('admin_db/tech/', admin_db_tech, name='AdminDbTech'),
     path('admin_db/user/', admin_db_user, name='AdminDbUser'),
     
     #* device manager
     path('dev_manager/', dev_manager, name='DevManager'),
     path('dev_manager/add', dev_manager_add, name='DevAdd'),
     path('dev_manager/details/<id>/', dev_manager_details, name='DevDetails'),
     path('dev_manager/edit/<id>/', dev_manager_edit, name='DevEdit'),
     path('dev_manager_delete/<id>/', dev_manager_delete, name='DevDelete'),


     path('pendings/', pending, name='Pending'),
     path('pendings/pendings_list/', pending_list, name='PendingList'),
     path('pendings/pendings_edit/<id>', pending_edit, name='PendingEdit'),

]

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from rest_framework import viewsets
from .serializers import ModelSerializer
from django.db.models import Q
from .functions import flag_dev
#Create your views here.

#* DJANGO REST VIEWS

# Django rest Models
class ModelViewset(viewsets.ModelViewSet):
     queryset = Model.objects.all()
     serializer_class = ModelSerializer

     def get_queryset(self):
          models = Model.objects.all()

          model = self.request.GET.get('model')

          if model:
               models = models.filter(model__contains=model)

          return models


#* HOME VIEW

# Home/Index view
def home(request): 
     pendings = Pendings.objects.all()
     searchP = request.GET.get('searchP')
     page = request.GET.get('page', 1)

     try:
          paginator = Paginator(pendings, 10)
          pendings = paginator.page(page)
     except:
          raise Http404

     if searchP:
          pendings = Pendings.objects.filter(
               Q(required_by__name__icontains = searchP) |
               Q(service_for__name__icontains = searchP) |
               Q(device__model__model__icontains = searchP) |
               Q(reason__icontains = searchP) |
               Q(state__status__icontains = searchP) 
          ).distinct()
     
     data = {
          'home_form': HomeForm(),
          'entity': pendings, 
          'paginator': paginator    
     }

     if request.method == 'POST':
          service_form = HomeForm(data=request.POST)
          if service_form.is_valid():
               service_form.save()
               data["message"] = "se ha enviado la solicitud"
          else:
               data['home_form'] = service_form

     return render(request, 'appsmartip/home.html', data)


#* REGISTRATION

def register(request):
     
     data = {
          'form': CustomUserCreationForm()
     }
     
     if request.method == 'POST':
          register_form = CustomUserCreationForm(data=request.POST)
          if register_form.is_valid():
               user = register_form.save()

               if Group.objects.contains['admins']:
                    group = Group.objects.get(name='admins')
                    user = authenticate(username=register_form.cleaned_data['username'], password=register_form.cleaned_data['password1'] )
                    user.groups.add(group)
               
               user = authenticate(username=register_form.cleaned_data['username'], password=register_form.cleaned_data['password1'] )
               login (request, user)
               messages.success(request, 'registro creado correctamente')
               return redirect(to='Home')
          data['form'] = register_form

     return render(request, 'registration/register.html', data)


#* ADMIN DB VIEWS

#* Dev Types

#* List Types
@permission_required('appsmartip.view_dev_type')
def admin_db_dev_type(request):
     dev_type_db_data = DevType.objects.all()

     data = {
          'dev_type_db_data': dev_type_db_data,
     }
     return render(request, 'appsmartip/admin_db/device_type/admin_db_dev_type.html', data)

#* CRUD

# Add Dev Type
@permission_required('appsmartip.add_dev_type')
def add_dev_type(request):
     data = {
          'add_dev_type_form': DevTypeFormAdd()
     }

     if request.method == 'POST':
          add_type_form = DevTypeFormAdd(data=request.POST)
          if add_type_form.is_valid():
               add_type_form.save()
               messages.success(request, 'Modelo Agregado correctamente')
               return redirect(to='AdminDbDevType')
          else:
               data['add_dev_type_form'] = add_type_form

     return render(request, 'appsmartip/admin_db/device_type/admin_db_add_dev_type.html', data)

# Delete Device Type
@permission_required('appsmartip.delete_dev_type')
def delete_dev_type(request, id):
     dev_type = get_object_or_404(DevType, id=id)
     dev_type.delete()
     messages.success(request, 'Eliminado correctamente')
     return redirect(to="AdminDbDevType")


# Edit Dev Type
@permission_required('appsmartip.change_dev_type')
def edit_dev_type(request, id):
     
     dev_type = get_object_or_404(DevType, id=id)
     
     data = {
          'edit_dev_type_form': DevTypeFormAdd(instance=dev_type),
     }

     if request.method == 'POST':
          edit_type_form = DevTypeFormAdd(data=request.POST, instance=dev_type)
          if edit_type_form.is_valid():
               edit_type_form.save()
               messages.success(request, 'Modificado correctamente')
               return redirect(to="AdminDbDevType")
          else:
               data['edit_dev_type_form'] = edit_type_form

     return render(request, 'appsmartip/admin_db/device_type/admin_db_modify_dev_type.html', data)

#* Dev Brands

#* List Brands
@permission_required('appsmartip.view_brand')
def admin_db_brand(request):
     brand = Brand.objects.all()

     data = {
          'brand': brand,
     }
     return render(request, 'appsmartip/admin_db/device_brands/brands.html', data)

#* CRUD
# Add Brand
@permission_required('appsmartip.add_dev_type')
def add_brand(request):
     data = {
          'brand': BrandFormAdd()
     }

     if request.method == 'POST':
          add_brand_form = BrandFormAdd(data=request.POST)
          if add_brand_form.is_valid():
               add_brand_form.save()
               messages.success(request, 'Marca Agregada correctamente')
               return redirect(to='AdminDbDevBrand')
          else:
               data['brand'] = add_brand_form

     return render(request, 'appsmartip/admin_db/device_brands/brand_add.html', data)

# Delete Brand
@permission_required('appsmartip.delete_brand')
def delete_brand(request, id):
     brand = get_object_or_404(Brand, id=id)
     brand.delete()
     messages.success(request, 'Eliminado correctamente')
     return redirect(to="AdminDbDevBrand")


# Edit Brand
@permission_required('appsmartip.change_dev_type')
def edit_brand(request, id):
     
     brand = get_object_or_404(Brand, id=id)
     
     data = {
          'edit_brand_form': BrandFormAdd(instance=brand),
     }

     if request.method == 'POST':
          edit_brand_form = BrandFormAdd(data=request.POST, instance=brand)
          if edit_brand_form.is_valid():
               edit_brand_form.save()
               messages.success(request, 'Modificado correctamente')
               return redirect(to="AdminDbDevBrand")
          else:
               data['brand'] = edit_brand_form

     return render(request, 'appsmartip/admin_db/device_brands/brand_edit.html', data)

#* Dev Models

#* List Models
@permission_required('appsmartip.view_model')
def list_dev_model(request):
     models = Model.objects.all()
     search_m = request.GET.get('searchM')
     page = request.GET.get('page', 1)

     try:
          paginator = Paginator (models, 8)
          models = paginator.page(page)
     except:
          raise Http404

     if search_m:
          models = Model.objects.filter(
               Q(model__icontains = search_m) |
               Q(img__icontains = search_m) 
          ).distinct()

     data = {
          'entity': models, 
          'paginator': paginator
     }

     return render(request, 'appsmartip/admin_db/device_model/admin_db_model.html', data)

# CRUD
# Add Model
@permission_required('appsmartip.add_model')
def add_dev_model(request):
     data = {
          'add_dev_model_form': DevModelFormAdd()
     }

     if request.method == 'POST':
          add_model_form = DevModelFormAdd(data=request.POST, files=request.FILES)
          if add_model_form.is_valid():
               add_model_form.save()
               messages.success(request, 'Modelo Agregado correctamente')
               return redirect(to='AdminDbDevModel')
          else:
               data['add_dev_model_form'] = add_model_form

     return render(request, 'appsmartip/admin_db/device_model/admin_db_model_add.html', data)

# Edit Model
@permission_required('appsmartip.change_model')
def edit_dev_model(request, id):
     
     model = get_object_or_404(Model, id=id)
     
     data = {
          'edit_model_form': DevModelFormAdd(instance=model),
          'model': model
     }

     if request.method == 'POST':
          edit_dev_model_form = DevModelFormAdd(data=request.POST, instance=model, files=request.FILES)
          if edit_dev_model_form.is_valid():
               edit_dev_model_form.save()
               messages.success(request, 'Modificado correctamente')
               return redirect(to="AdminDbDevModel")
          else:
               data['edit_model_form'] = edit_dev_model_form

     return render(request, 'appsmartip/admin_db/device_model/admin_db_model_modify.html', data)

# Delete Model
@permission_required('appsmartip.delete_model')
def delete_dev_model(request, id):
     model = get_object_or_404(Model, id=id)
     model.delete()
     messages.success(request, 'Eliminado correctamente')
     return redirect(to="AdminDbDevModel")

#* Ip views

# List Ip
@permission_required('appsmartip.view_ip')
def list_ips(request):
     ips = Ip.objects.all()
     searchIp = request.GET.get('searchIp')
     page = request.GET.get('page', 1)

     try:
          paginator = Paginator (ips, 10)
          ips = paginator.page(page)
     except:
          raise Http404

     if searchIp:
          ips = Ip.objects.filter(
               Q(ipdir__icontains = searchIp) |
               Q(internet_access__access_type__icontains = searchIp) 
          ).distinct()     

     data = { 
          'entity': ips,
          'paginator': paginator
     }

     return render(request, 'appsmartip/admin_db/ip/list_ips.html', data)

#* CRUD
# Add Ip

def add_ip(request):
     data = {
          'ip_form_add':IpAddForm()
     }

     if request.method == 'POST':
          ip_add = IpAddForm(data=request.POST)
          if ip_add.is_valid():
               ip_add.save()
               messages.success(request, 'Direccion IP agregada correctamente')
               return redirect(to='IpHome')
          else:
               data['ip_form_add'] = ip_add

     return render(request, 'appsmartip/admin_db/ip/add_ip.html', data)

# Delete Ip
@permission_required('appsmartip.delete_ip')
def delete_ip(request, id):
     ipdir = get_object_or_404(Ip, id=id)
     ipdir.delete()
     messages.success( request, 'Direccion Ip Eliminada Correctamente')
     return redirect(to='IpHome')

# Edit Ip
def edit_ip(request, id):
     ipdir = get_object_or_404(Ip, id=id)
     data = {
          'ipdir_edit_form': IpAddForm(instance=ipdir)
     }

     if request.method == 'POST':
          ipdir_edit = IpAddForm(data=request.POST, instance=ipdir)
          if ipdir_edit.is_valid():
               ipdir_edit.save()
               messages.success(request, 'La direccion ip se ha actualizado correctamente')
               return redirect(to='IpHome')
          else:
               data['ipdir_edit_form'] = ipdir_edit

     return render(request, 'appsmartip/admin_db/ip/edit_ip.html', data)

#* Internet Access Types
# List Internet Access Types
@permission_required('appsmartip.view_ip')
def list_access(request):
     access_type = Internet.objects.all()

     data = {
          'access_type': access_type
     }
     return render(request, 'appsmartip/admin_db/internet_access/internet.html', data)

#* CRUD
# Internet Access Add
@permission_required('appsmartip.add_internet')
def add_access(request):
     data = {
          'access_type': InternetAccessAddForm() 
     }

     if request.method == 'POST':
          add_access_type = InternetAccessAddForm(data=request.POST)
          if add_access_type.is_valid():
               add_access_type.save()
               messages.success(request, 'Tipo de acceso agregado correctamente')
               return redirect(to='InAccessList')
          else:
               data['access_type'] = add_access_type

     return render(request, 'appsmartip/admin_db/internet_access/internet_add.html', data)

# Edit Internet Access
@permission_required('appsmartip.modify_internet')
def edit_access(request, id):
     access_type = get_object_or_404(Internet, id=id)
     
     data = {
          'edit_access_type_form': InternetAccessAddForm(instance=access_type)
     }

     if request.method == 'POST':
          edit_access_type = InternetAccessAddForm(data=request.POST, instance=access_type)
          if edit_access_type.is_valid():
               edit_access_type.save()
               messages.success(request, 'Tipo de accesso editado exitosamente')
               return redirect(to='InAccessList')
          else:
               data['edit_access_type_form'] = edit_access_type

     return render(request, 'appsmartip/admin_db/internet_access/internet_edit.html', data)

#  Delete Internet Access
@permission_required('appsmartip.delete_internet')
def delete_access(request, id):
     access_type = get_object_or_404(Internet, id=id)
     access_type.delete()
     messages.success(request, 'Tipo de Acceso Eliminado Correctamente')
     return redirect(to='InAccessList')

#* Locations
#* List Locations
def admin_db_location(request):
     locations = Location.objects.all()
     data = {
          'locations': locations
     }

     return render(request, 'appsmartip/admin_db/location/location.html', data)

#* CRUD

#* Add Location
def location_add(request):
     data = {
          'location_add_form':LocationAddForm()
     }

     if request.method == 'POST':
          location_form = LocationAddForm(data=request.POST)
          if location_form.is_valid():
               location_form.save()
               messages.success(request, 'Localidad agregada exitosamente')
               return redirect(to='Location')
          else:
               data['location_add_form'] = location_form


     return render(request, 'appsmartip/admin_db/location/location_add.html', data)

#* Edit Location
@permission_required('appsmartip.modify_location')
def location_edit(request, id):
     location = get_object_or_404(Location, id=id)

     data = {
          'location_edit_form': LocationAddForm(instance=location)
     }

     if request.method == 'POST':
          location_form_edit = LocationAddForm(data=request.POST, instance=location)
          
          if location_form_edit.is_valid():
               location_form_edit.save()
               messages.success(request, 'Localidad modificada correctamente')
               return redirect(to='Location')
          else:
               data['location_edit_form'] = location_form_edit

     return render(request, 'appsmartip/admin_db/location/location_edit.html', data)


#* Delete Location
@permission_required('appsmartip.delete_location')
def location_delete(request, id):
     location = get_object_or_404(Location, id=id)
     location.delete()
     messages.success(request, 'Localidad eliminada correctamente')
     return redirect(to='Location')

#* EDIFFICES VIEWS
#* Ediffices List
@permission_required('appsmartip.view_edifice')
def admin_db_ediffice(request):
     ediffices = Edifice.objects.all()
     data = {
          'ediffices': ediffices
     }
     return render(request, 'appsmartip/admin_db/ediffices/ediffices.html', data)

#* Ediffices Add
@permission_required('appsmartip.add_edifice')
def ediffice_add(request):
     data = {
          'ediffice_add_form': EdifficeAddForm(data=request.POST)
     }

     if request.method == 'POST':
          ediffice_add = EdifficeAddForm(data=request.POST)

          if ediffice_add.is_valid():
               ediffice_add.save()
               messages.success(request, 'Edificio agregado correctamente')
               return redirect(to='Ediffices')
          else:
               data['ediffice_add_form'] = ediffice_add

     return render(request, 'appsmartip/admin_db/ediffices/ediffices_add.html', data)

#* Edit Location
@permission_required('appsmartip.modify_edifice')
def ediffice_edit(request, id):
     ediffice = get_object_or_404(Edifice, id=id)
     data={
          'ediffice_edit_form': EdifficeAddForm(instance=ediffice)
     }
     
     if request.method == 'POST':
          ediffice_edit = EdifficeAddForm(data=request.POST, instance=ediffice)
          
          if ediffice_edit.is_valid():
               ediffice_edit.save()
               messages.success(request, 'Edificio editado correctemente')
               return redirect(to='Ediffices')
          else:
               data['ediffice_edit_form'] = ediffice_edit
     
     return render(request, 'appsmartip/admin_db/ediffices/ediffices.edit.html', data)

#* Delete Ediffice
@permission_required('appsmartip.delete_edifice')
def ediffice_delete(request, id):
     edifice = get_object_or_404(Edifice, id=id)
     edifice.delete()
     messages.success(request, 'Edificio eliminado correctamente')
     return redirect(to='Ediffices')

#* OFFICES VIEWS
#* Offices list
@permission_required('appsmartip.view_office')
def admin_db_offices(request):

     offices = Office.objects.all()
     search_of = request.GET.get('searchOffice')
     page = request.GET.get('page', 1)

     try:
          paginator = Paginator (offices, 10)
          offices = paginator.page(page)
     except:
          raise Http404

     if search_of:     
          offices = Office.objects.filter(
               Q(location__location__icontains = search_of) |
               Q(edifice__edifice__icontains = search_of) |
               Q(floor__icontains = search_of) |
               Q(court__court__icontains = search_of) |
               Q(office_name__icontains = search_of) |
               Q(phone_1__icontains = search_of) |
               Q(phone_2__icontains = search_of) |
               Q(phone_3__icontains = search_of) 
          ).distinct()
     
     data = {
          'entity': offices, 
          'paginator': paginator
     }
     return render(request, 'appsmartip/admin_db/offices/offices.html', data)

#* Office Details
@permission_required('appsmartip.view_office')
def office_details(request, id):
     office = get_object_or_404(Office, id=id)
     device = Device.objects.all()
          
     devices_office = device.filter(office_id=office.id)
     
     flag = flag_dev(devices_office)
     

     data = {
          'office': office,
          'device_office': devices_office,
          'flag': flag
     }

     return render(request, 'appsmartip/admin_db/offices/offices_details.html', data)

#* CRUD
#* Office Add
@permission_required('appsmartip.add_office')
def offices_add(request):
     data = {
          'office_add':OfficeFormAdd()
     }

     if request.method == 'POST':
          offices_add_form = OfficeFormAdd(data=request.POST)

          if offices_add_form.is_valid():
               offices_add_form.save()
               messages.success(request,'Oficina agregada correctamente')
               return redirect(to='Offices')
          else:
               data['office_add'] = offices_add_form

     return render(request, 'appsmartip/admin_db/offices/offices_add.html', data)

#* Office Edit
@permission_required('appsmartip.modify_office')
def offices_edit(request, id):
     office = get_object_or_404(Office, id=id)
     data = {
          'office_edit_form': OfficeFormAdd(instance=office)
     }

     if request.method == 'POST':
          office_edit = OfficeFormAdd(request.POST, instance=office)

          if office_edit.is_valid():
               office_edit.save()
               messages.success(request, 'La oficina se ha editado correctamente')
               return redirect(to='Offices')
          else:
               data['office_edit_form'] = office_edit

     return render(request, 'appsmartip/admin_db/offices/offices_edit.html', data)

#* Office Delete
permission_required('appsmartip.delelte_office')
def office_delete(request, id):
     office = get_object_or_404(Office, id=id)
     office.delete()
     messages.success(request,'Oficina eliminada correctamente')
     return redirect(to='Offices')

#* Device Status
#* List Devices Status
permission_required('appsmartip.view_dev_status')
def admin_db_dev_status(request):
     dev_status = DevStatus.objects.all()

     data = {
          'dev_status': dev_status
     }

     return render(request, 'appsmartip/admin_db/device_status/admin_db_dev_status.html', data)

#* CRUD
#* Dev Staus Add
permission_required('appsmartip.add_dev_status')
def add_dev_status(request):
     data = {
          'dev_status_form_add': DevStatusFormAdd()
     }

     if request.method == 'POST':
          dev_status_add = DevStatusFormAdd(data=request.POST)

          if dev_status_add.is_valid():
               dev_status_add.save()
               messages.success(request, 'Nuevo estado agregado correctamente')
               return redirect(to='DevStatusAdd')
          else:
               data['dev_status_form_add'] = dev_status_add

     return render(request, 'appsmartip/admin_db/device_status/admin_db_dev_status_add.html', data)

#* Dev Status Edit
permission_required('appsmartip.modify_dev_status')
def edit_dev_status(request, id):
     dev_status = get_object_or_404(DevStatus, id=id)
     data = {
          'dev_status_edit_form': DevStatusFormAdd(instance=dev_status)
     }

     if request.method == 'POST':
          dev_status_edit = DevStatusFormAdd(request.POST, instance=dev_status)

          if dev_status_edit.is_valid():
               dev_status_edit.save()
               messages.success(request, 'El estado se ha modificado correctamente')
               return redirect(to='DevStatus')
          else:
               data['dev_status_edit_form'] = dev_status_edit

     return render(request, 'appsmartip/admin_db/device_status/admin_db_dev_status_edit.html', data)

#* Dev Status Delete
permission_required('appsmartip.delete_dev_status')
def delete_dev_status(request, id):
     dev_status = get_object_or_404(DevStatus, id=id)
     dev_status.delete()
     messages.success(request, 'El estado se ha eliminado correctamente')
     return redirect(to='DevStatus')

#* Pending Status
#* List Pending Status
permission_required('appsmartip.view_pending_status')
def admin_db_pen_status(request):
     pending_status = PendingStatus.objects.all()

     data = {
          'pending_status': pending_status
     }

     return render(request, 'appsmartip/admin_db/pendings_status/admin_db_pen_status.html', data)

#* CRUD
#* Pending Staus Add
permission_required('appsmartip.add_pending_status')
def add_pen_status(request):
     data = {
          'pending_status_form_add': PendingStatusFormAdd()
     }

     if request.method == 'POST':
          pending_status_add = PendingStatusFormAdd(data=request.POST)

          if pending_status_add.is_valid():
               pending_status_add.save()
               messages.success(request, 'Nuevo estado agregado correctamente')
               return redirect(to='PendingStatusAdd')
          else:
               data['pending_status_form_add'] = pending_status_add

     return render(request, 'appsmartip/admin_db/pendings_status/admin_db_pen_status_add.html', data)

#* Pending Status Edit
permission_required('appsmartip.modify_pending_status')
def edit_pen_status(request, id):
     pending_status = get_object_or_404(PendingStatus, id=id)
     data = {
          'pending_status_edit_form': PendingStatusFormAdd(instance=pending_status)
     }

     if request.method == 'POST':
          pending_status_edit = PendingStatusFormAdd(request.POST, instance=pending_status)

          if pending_status_edit.is_valid():
               pending_status_edit.save()
               messages.success(request, 'El estado se ha modificado correctamente')
               return redirect(to='PendingStatus')
          else:
               data['pending_status_edit_form'] = pending_status_edit

     return render(request, 'appsmartip/admin_db/pendings_status/admin_db_pen_status_edit.html', data)

#* Pending Status Delete
permission_required('appsmartip.delete_pending_status')
def delete_pen_status(request, id):
     pending_status = get_object_or_404(PendingStatus, id=id)
     pending_status.delete()
     messages.success(request, 'El estado se ha eliminado correctamente')
     return redirect(to='PendingStatus')

#* Technicals
#* List Technicals
permission_required('appsmartip.view_tech')
def technicals(request):
     technicals = Tech.objects.all()

     data = {
          'technicals': technicals
     }

     return render(request, 'appsmartip/admin_db/techs/technicals.html', data)

#* CRUD
#* Technical Add
permission_required('appsmartip.add_tech')
def add_technical(request):
     data = {
          'technical_form_add': TechFormAdd()
     }

     if request.method == 'POST':
          technical_add = TechFormAdd(data=request.POST)

          if technical_add.is_valid():
               technical_add.save()
               messages.success(request, 'El nuevo tecnico se ha agregado correctamente')
               return redirect(to='TechAdd')
          else:
               data['technical_form_add'] = technical_add

     return render(request, 'appsmartip/admin_db/techs/technicals_add.html', data)

#* Technical Edit
permission_required('appsmartip.modify_tech')
def edit_technical(request, id):
     technical = get_object_or_404(Tech, id=id)
     data = {
          'technical_edit_form': TechFormAdd(instance=technical)
     }

     if request.method == 'POST':
          technical_edit = TechFormAdd(request.POST, instance=technical)

          if technical_edit.is_valid():
               technical_edit.save()
               messages.success(request, 'El tecnico se ha modificado correctamente')
               return redirect(to='Technicals')
          else:
               data['technical_edit_form'] = technical_edit

     return render(request, 'appsmartip/admin_db/techs/technicals_edit.html', data)

#* Technical Delete
permission_required('appsmartip.delete_tech')
def delete_technical(request, id):
     technical = get_object_or_404(Tech, id=id)
     technical.delete()
     messages.success(request, 'El tecnico se ha eliminado correctamente')
     return redirect(to='Technicals')

#* DEVICE USERS
# * Device Users list
@permission_required('appsmartip.view_dev_users')
def admin_db_dev_users(request):

     dev_users = DevUsers.objects.all()
     search_du = request.GET.get('searchDevUser')
     page = request.GET.get('page', 1)

     try:
          paginator = Paginator(dev_users, 10)
          dev_users = paginator.page(page)
     except:
          raise Http404 
     
     if search_du:
          dev_users = DevUsers.objects.filter(
               Q(name__icontains=search_du) |
               Q(last_name__icontains=search_du) |
               Q(email__icontains=search_du) |
               Q(message_account__icontains=search_du) |
               Q(message_pass__icontains=search_du) |
               Q(username__icontains=search_du) 
          ).distinct()

     data = {
          'entity': dev_users,
          'paginator': paginator
     }
     return render(request, 'appsmartip/admin_db/device_users/dev_users.html', data)

# * Dev User Details
@permission_required('appsmartip.view_dev_user')
def dev_user_details(request, id):
     user = get_object_or_404(DevUsers, id=id)
     device = Device.objects.all()

     devices_user = device.filter(user_id=user.id)

     flag = flag_dev(devices_user)

     data = {
          'user': user,
          'device_user': devices_user,
          'flag': flag,
     }

     return render(request, 'appsmartip/admin_db/ediffices/user_details.html', data)

#! CRUD   
#* Add Device User
permission_required('appsmartip.add_dev_user')
def add_dev_user(request):
     data = {
          'dev_user_form_add': DevUsersFormAdd()
     }

     if request.method == 'POST':
          dev_user_add = DevUsersFormAdd(data=request.POST)

          if dev_user_add.is_valid():
               dev_user_add.save()
               messages.success(request, 'El nuevo usuario de dispositivo se ha agregado correctamente')
               return redirect(to='DevUserAdd')
          else:
               data['dev_user_form_add'] = dev_user_add

     return render(request, 'appsmartip/admin_db/device_users/dev_user_add.html', data)

#* Edit Device User
permission_required('appsmartip.modify_dev_user')
def edit_dev_user(request, id):
     dev_user = get_object_or_404(DevUsers, id=id)

     data = {
          'dev_user_form_edit': DevUsersFormAdd(instance=dev_user)
     }

     if request.method == 'POST':
          dev_user_edit = DevUsersFormAdd(request.POST, instance=dev_user)

          if dev_user_edit.is_valid():
               dev_user_edit.save()
               messages.success(request, 'El usuario de dispositivo se ha modificado correctamente')
               return redirect(to='DevUsers')
          else:
               data['dev_user_form_edit'] = dev_user_edit

     return render(request, 'appsmartip/admin_db/device_users/dev_user_edit.html', data)

#* Delete Device User
permission_required('appsmartip.delete_dev_user')
def delete_dev_user(request, id):
     dev_user = get_object_or_404(DevUsers, id=id)
     dev_user.delete()
     messages.success(request, 'El usuario de dispositivo se ha eliminado correctamente')
     return redirect(to='DevUsers')


def admin_db_pend_status(request):
     return render(request, 'appsmartip/admin_db_status.html')

#Pendings Views
def pending(request):
     return render(request, 'appsmartip/agenda/pending.html')

#! List Pendings
@permission_required('appsmartip.view_pendings')
def pending_list(request):
     pendings = Pendings.objects.all()

     data = {
          'pendings': pendings
     }

     return render(request, 'appsmartip/agenda/pending_list.html', data)

def pending_edit(request, id):
     return render(request, 'appsmartip/agenda/pending_edit.html')



#* DEVICE MANAGER VIEWS

#* Device Details
@permission_required('appsmartip.view_device')
def dev_manager_details (request, id):
     device = get_object_or_404(Device, id=id)

     data = {
          'device':device
     }

     return render(request, 'appsmartip/device_manager/device_details.html', data)


#* CRUD

#* Dev Manager List Devices
def dev_manager(request):
     device = Device.objects.all()
     search = request.GET.get('search')
     
     if search:
          device = Device.objects.filter(
               Q(dev_name__icontains = search) |
               Q(dev_type__dev_type__icontains = search) |
               Q(brand__brand__icontains = search) |
               Q(model__model__icontains = search) |
               Q(ip_direction__ipdir__icontains = search) |
               Q(last_revision__icontains = search) |
               Q(cause__icontains = search) |
               Q(has_user__icontains = search) |
               Q(user__last_name__icontains = search) |
               Q(office__office_name__icontains = search) 
          ).distinct()

     data = {
          'device':device
     }

     return render(request, 'appsmartip/device_manager/dev_manager.html', data)

#* Add Device
@permission_required('appsmartip.add_device')
def dev_manager_add(request):
     data = {
          'add_device': DeviceFormAdd()
     }

     if request.method == 'POST':
          add_device_form = DeviceFormAdd(data=request.POST)
          if add_device_form.is_valid():
               add_device_form.save()
               messages.success(request, 'Dispositivo agregado correctamente')
               return redirect(to="DevManager")
          else:
               data['add_device'] = add_device_form

     return render(request, 'appsmartip/device_manager/device_add.html', data)


#* Edit Device
@permission_required('appsmartip.change_device')
def dev_manager_edit(request, id):
     
     device = get_object_or_404(Device, id=id)
     
     data = {
          'edit_device': DeviceFormAdd(instance=device)
     }

     if request.method == 'POST':
          edit_device_form = DeviceFormAdd(data=request.POST, instance=device)
          if edit_device_form.is_valid():
               edit_device_form.save()
               messages.success(request, 'Modificado correctamente')
               return redirect(to="DevManager")
          else:
               data['edit_device'] = edit_device_form

     return render(request, 'appsmartip/device_manager/device_edit.html', data)


#* Delete Device
@permission_required('appsmartip.delete_device')
def dev_manager_delete(request, id):
     device = get_object_or_404(Device, id=id)
     device.delete()
     messages.success(request, 'Eliminado correctamente')
     return redirect(to='DevManager')
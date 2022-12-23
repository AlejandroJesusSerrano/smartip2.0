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

# List Models
@permission_required('appsmartip.view_model')
def list_dev_model(request):
     models = Model.objects.all()
     searchM = request.GET.get('searchM')
     page = request.GET.get('page', 1)

     try:
          paginator = Paginator (models, 8)
          models = paginator.page(page)
     except:
          raise Http404

     if searchM:
          models = Model.objects.filter(
               Q(model__icontains = searchM) |
               Q(img__icontains = searchM) 
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

#? List Ip
@permission_required('appsmartip.view_ip')
def list_ips(request):
     ips = Ip.objects.all()

     data = { 
          'ips': ips
     }

     return render(request, 'appsmartip/admin_db/ip/list_ips.html', data)

# CRUD
# Add Ip
def add_ip(request):
     return render(request, 'appsmartip/admin_db/ip/add_ip.html')


#! Internet Access Types
#? List Internet Access Types
@permission_required('appsmartip.view_internet')
def list_access(request):
     internet = Internet.objects.all()

     data = {
          'internet': internet
     }
     return render(request, 'appsmartip/admin_db/internet_access/internet.html', data)

#? CRUD
# Internet Access Add
@permission_required('appsmartip.add_internet')
def add_access(request):
     data = {
          'access_type_form': InternetAccessAddForm() 
     }

     if request.method == 'POST':
          add_access_type = InternetAccessAddForm(data=request.POST)
          if add_access_type.is_valid():
               add_access_type.save()
               messages.success('Tipo de acceso agregado correctamente')
               return redirect(to='InAccessList')
          else:
               data['access_type_form'] = add_access_type

     return render(request, 'appsmartip/admin_db/internet_access/internet_add.html')




def admin_db(request):
     return render(request, 'appsmartip/admin_db.html')

def admin_db_location(request):
     return render(request, 'appsmartip/admin_db_location.html')

def admin_db_ediffice(request):
     return render(request, 'appsmartip/admin_db_ediffice.html')

def admin_db_office(request):
     return render(request, 'appsmartip/admin_db_office.html')

def admin_db_status(request):
     return render(request, 'appsmartip/admin_db_status.html')

def admin_db_tech(request):
     return render(request, 'appsmartip/admin_db_tech.html')

def admin_db_user(request):
     return render(request, 'appsmartip/admin_db_user.html')

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
               return redirect(to="DevAdd")
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
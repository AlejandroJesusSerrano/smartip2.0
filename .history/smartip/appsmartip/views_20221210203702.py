from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
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




# Home/Index view
def home(request): 
     pendings = Pendings.objects.all()
     
     
     page = request.GET.get('page', 1)

     try:
          paginator = Paginator(pendings, 10)
          pendings = paginator.page(page)
     except:
          raise Http404

     
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

def add_dev_type(request):
     data = {
          'add_dev_type_form': DevTypeFormAdd()
     }

     return render(request, 'appsmartip/admin_db/device_type/admin_db_add_dev_type.html', data)

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



#* DEVICE MODELS VIEWS

# Home Menu
@permission_required('appsmartip.view_model')
def dev_models(request):
     return render(request, 'appsmartip/admin_db/device_model/admin_db_model.html')

# List Models
@permission_required('appsmartip.view_model')
def list_dev_model(request):
     models = Model.objects.all()
     page = request.GET.get('page', 1)

     try:
          paginator = Paginator (models, 10)
          models = paginator.page(page)
     except:
          raise Http404

     data = {
          'entity': models, 
          'paginator': paginator
     }

     return render(request, 'appsmartip/admin_db/device_model/admin_db_model_list.html', data)

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
               data["message"] = 'Modelo de Dispositivo agregado correctamente'
          else:
               data['add_dev_model_form'] = add_model_form

     return render(request, 'appsmartip/admin_db/device_model/admin_db_model_add.html', data)

# Edit Model
@permission_required('appsmartip.change_model')
def edit_dev_model(request, id):
     
     model = get_object_or_404(Model, id=id)
     
     data = {
          'edit_model_form': DevModelFormAdd(instance=model)
     }

     if request.method == 'POST':
          edit_dev_model_form = DevModelFormAdd(data=request.POST, instance=model, files=request.FILES)
          if edit_dev_model_form.is_valid():
               edit_dev_model_form.save()
               messages.success(request, 'Modificado correctamente')
               return redirect(to="AdminDevModelList")
          else:
               data['edit_model_form'] = edit_dev_model_form


     return render(request, 'appsmartip/admin_db/device_model/admin_db_model_modify.html', data)

# Delete Model
@permission_required('appsmartip.delete_model')
def delete_dev_model(request, id):
     model = get_object_or_404(Model, id=id)
     model.delete()
     messages.success(request, 'Eliminado correctamente')
     return redirect(to="AdminDevModelList")



# Admin DB Views
def admin_db(request):
     return render(request, 'appsmartip/admin_db.html')

def admin_db_location(request):
     return render(request, 'appsmartip/admin_db_location.html')

def admin_db_ediffice(request):
     return render(request, 'appsmartip/admin_db_ediffice.html')

def admin_db_office(request):
     return render(request, 'appsmartip/admin_db_office.html')

def admin_db_dev_type(request):
     return render(request, 'appsmartip/admin_db_dev_type.html')

def admin_db_status(request):
     return render(request, 'appsmartip/admin_db_status.html')

def admin_db_tech(request):
     return render(request, 'appsmartip/admin_db_tech.html')

def admin_db_user(request):
     return render(request, 'appsmartip/admin_db_user.html')

#Pendings Views
def pending(request):
     return render(request, 'appsmartip/agenda/pending.html')

# List Pendings
# @permission_required('appsmartip.view_pendings')
def pending_list(request):
     pendings = Pendings.objects.all()

     data = {
          'pendings': pendings
     }
     # page = request.GET.get('page', 1)

     # try:
     #      paginator = Paginator (pendings, 10)
     #      pendings = paginator.page(page)
     # except:
     #      raise Http404

     # data = {
     #      'entity': pendings, 
     #      'paginator': paginator
     # }

     return render(request, 'appsmartip/agenda/pending_list.html', data)

def pending_edit(request, id):
     return render(request, 'appsmartip/agenda/pending_edit.html')


#Devices Manager Views
def dev_manager(request):
     device = Device.objects.all()
     search = request.GET.get("search")
     
     if search:
          device = Device.objects.filter(
               Q(dev_name__icontains = search) |
               Q(dev_type__icontains = search) |
               Q(brand__icontains = search) |
               Q(model__icontains = search) |
               Q(ip_direction__icontains = search) |
               Q(last_revision__icontains = search) |
               Q(cause__icontains = search) |
               Q(tech_revision__icontains = search) |
               Q(has_user__icontains = search) |
               Q(user__icontains = search) |
               Q(office__icontains = search) 
          ).distinct()

     data = {
          'device':device
     }
     return render(request, 'appsmartip/device_manager/dev_manager.html', data)

def dev_manager_filtred_result(request):
     return render(request, 'appsmartip/device_manager/dev_manager_filtred_result.html')

def device_details(request):
     return render(request, 'appsmartip/device_manager/device_details.html')


#Search Views
def search(request):
     return render(request, 'appsmartip/search.html')

def search_dev(request):
     return render(request, 'appsmartip/search_dev.html')

def search_dev_result(request):
     return render(request, 'appsmartip/search_dev_result.html')

def search_ip(request):
     return render(request, 'appsmartip/search_ip.html')

def search_office(request):
     return render(request, 'appsmartip/search_office.html')

def search_office_result(request):
     return render(render, 'appsmartip/search_office_result.html')

def search_result_detail(request):
     return render(request, 'appsmartip/search_result_detail.html')

def search_user(request):
     return render(request, 'appsmartip/search_user.html')

def search_user(request):
     return render(request, 'appsmartip/search_user.html')

def search_user_result(request):
     return render(request, 'appsmartip/search_user_result')

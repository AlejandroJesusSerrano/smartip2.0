from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group

# Home/Index view
def home(request):
     data = {
          'home_form': HomeForm()
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

# REGISTRATION

def register(request):
     
     data = {
          'form': CustomUserCreationForm()
     }
     
     if request.method == 'POST':
          register_form = CustomUserCreationForm(data=request.POST)
          if register_form.is_valid():
               user = register_form.save()
               group = Group.objects.get(name='admins')
               user = authenticate(username=register_form.cleaned_data['username'], password=register_form.cleaned_data['password1'] )
               user.groups.add(group)
               login (request, user)
               messages.success(request, 'registro creado correctamente')
               return redirect(to='Home')
          data['form'] = register_form

     return render(request, 'registration/register.html', data)



# DEVICE MODELS VIEWS

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
     return render(request, 'appsmartip/pending.html')

#Devices Manager Views
def dev_manager(request):
     return render(request, 'appsmartip/dev_manager.html')

def dev_manager_filtred_result(request):
     return render(request, 'appsmartip/dev_manager_filtred_result.html')

def device_details(request):
     return render(request, 'appsmartip/device_details.html')

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
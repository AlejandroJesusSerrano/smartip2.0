from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

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


     return render(request, 'appsmartip/home.html')





















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

from django.shortcuts import render

# Create your views here.

# Home/Index view
def home(request):
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
     return render(request, 'appsamrtip/admin_db_user.html')

#Pendings Views
def pending(request):
     return render(request, 'appsmartip/pending.html')

#Devices Manager Views
def dev_manager_listed(request):
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

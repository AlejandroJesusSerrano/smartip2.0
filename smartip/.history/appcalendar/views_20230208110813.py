from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def calendar_view (request):
    return render (request, 'appcalendar/calendar.html')
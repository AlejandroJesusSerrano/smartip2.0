from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def calendar (request):
    return render (request, 'appcalendar/calendar.html')

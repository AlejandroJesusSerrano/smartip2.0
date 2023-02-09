from django.shortcuts import render
from django.views.generic import View
from .models import Pendings

# Create your views here.

class CalendarView(View):
    
    def calendar (self, request):
        return render (request, 'appcalendar/calendar.html')

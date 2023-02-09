from django.shortcuts import render
from .models import Pendings

# Create your views here.

class CalendarView(ListView):
    model = Pendings
    template_name = "appcalendar/calendar.html"

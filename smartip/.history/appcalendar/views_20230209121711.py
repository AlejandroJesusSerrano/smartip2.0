from django.shortcuts import render
from django.views.generic import ListView
from .models import Pendings
# Create your views here.


class Calendar(ListView):
    model = Pendings
    template_name = 'appcalendar/calendar.html'
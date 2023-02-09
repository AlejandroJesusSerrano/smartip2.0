from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def calendar(request):
    
    suma = 5+5
    
    data={
        'Vista':'Calendario',
        'App':'Calendario',
        'Suma': suma
    }

    return render (request, '/appcalendar/calendar.html', data)
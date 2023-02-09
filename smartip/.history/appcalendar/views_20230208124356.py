from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def calendar(request):
    template = loader.get_template('calendar.html')
    suma = 5+5
    data={
        'Vista':'Calendario',
        'App':'Calendario',
        'Suma': suma
    }

    return HttpResponse(template.render(data, request))
from django.shortcuts import render
from django.views.generic import ListView
from .models import Pendings
# Create your views here.


class Calendar(ListView):
    model = Pendings
    template_name = 'appcalendar/calendar.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(state = 1, service_for = self.request.service_for.last_name, office = self.request.office_name)
        return queryset
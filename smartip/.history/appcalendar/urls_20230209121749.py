from django.urls import path
from .views import *

urlpatterns = [
    path('task_calendar/', Calendar, name='Calendar')
]
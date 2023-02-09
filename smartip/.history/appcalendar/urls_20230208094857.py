from django.urls import path
from .views import *

path('tasker', CalendarView, name='TaskManager')
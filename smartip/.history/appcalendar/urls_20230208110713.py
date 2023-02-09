from django.urls import path
from .views import *

path('tasker/', CalendarView.as_view(), name='TaskManager')
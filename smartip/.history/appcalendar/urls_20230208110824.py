from django.urls import path
from .views import *

path('tasker/', calendar_view, name='TaskManager')
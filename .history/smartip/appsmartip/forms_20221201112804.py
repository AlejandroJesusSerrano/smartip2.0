from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class HomeForm(forms.ModelForm):
     class Meta:
          model = Pendings
          fields = ['required_by', 'personal', 'service_for', 'device', 'reason']
     


class DevTypeFormAdd(forms.ModelForm):
     class Meta:
          model = DevType
          fields = '__all__'


class DevModelFormAdd(forms.ModelForm):
     class Meta:
          model = Model
          fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
     
     class Meta:
          model = User

          if User.is_authenticated:
               fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'groups' ]
          else:
               fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]


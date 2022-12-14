from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from .validators import MaxSizeFileValidator


class HomeForm(forms.ModelForm):
     class Meta:
          model = Pendings
          fields = ['required_by', 'personal', 'service_for', 'device', 'reason']
     


class DevTypeFormAdd(forms.ModelForm):
     class Meta:
          model = DevType
          fields = '__all__'


class DevModelFormAdd(forms.ModelForm):

     def clean_model(self)
          model = self.cleaned_data['model']
          is_in = Model.objects.filter(model__iexact=model).exists()

          if is_in:
               raise ValidationError('Este modelo ya se encuentra en la Base de Datos')

          return model

     img = forms.ImageField(required=True, validators=[MaxSizeFileValidator(max_file_size=5)])
     class Meta:
          model = Model
          fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
     
     class Meta:
          model = User
          fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


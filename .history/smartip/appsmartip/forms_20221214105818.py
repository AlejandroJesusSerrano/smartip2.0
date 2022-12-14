from django.contrib import admin
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from .validators import MaxSizeFileValidator
from ckeditor.widgets import CKEditorWidget

class HomeForm(forms.ModelForm):
     reason=forms.CharField(widget=CKEditorWidget())
     class Meta:
          model = Pendings
          fields = ['required_by', 'personal', 'service_for', 'device', 'reason']
          labels = {
               'required_by': ('Requerido por: '),
               'service_for': ('Servicio para: '),
               'device': ('Dispositivo: '),
               'reason': ('Motivo'),
          }
          help_texts = {
               'required_by': ('Seleccione el usuario que esta solicitando el servicio tecnico'),
               'service_for': ('Seleccione el usuario para el cual es el servicio'),
               'device': ('Seleccione el dispositivo que presenta inconvenientes')
          }
          widgets = {
               'required_by': forms.Select(attrs={
                    'class': 'form-control', 
                    'id':'required_by',

               }),

               'service_for':forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'service_for',
               }), 

               'device': forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'device',
               }), 

               'reason': forms.Textarea(attrs={
                    'class': 'form-control',
                    'id': 'reason',
                    'placeholder': "Ingrese la descripción del problema"
               })
          }     

#Device Type Form
class DevTypeFormAdd(forms.ModelForm):
     class Meta:
          model = DevType
          fields = '__all__'

#Device Models Form
class DevModelFormAdd(forms.ModelForm):

     def clean_model(self):
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


#Device Form
class DeviceFormAdd(forms.ModelForm):

     def clean_device(self):
          model = self.cleaned_data['device']
          is_in = Device.objects.filter(device__iexact=model).exists()

          if is_in:
               raise ValidationError('Este modelo ya se encuentra en la Base de Datos')

          return model
     
     
     class Meta:
          model = Device
          fields = '__all__'
          labels = {
               'dev_name': ('Nombre del dispositivo: '),
               'dev_type': ('Tipo de dispositivo: '),
               'brand': ('Marca: '),
               'model': ('Modelo'),
               'is_active': ('Esta Activo'),
               'is_working': ('Funciona'),
               'ip_direction': ('Direccion Ip'),
               'last_revision': ('Fecha de la última revision'),
               'cause': ('Motivo de la revision'),
               'tech_revision': ('Tecnico'),
               'has_user': ('Tiene usuario asignado'),
               'user': ('Usuario asignado'),
               'office': ('Oficina')

          }
          help_texts = {
               'dev_name': ('Ingrese el nombre con el que el dispositivo se encuentra registrado en dominio'),
               'service_for': ('Seleccione el usuario para el cual es el servicio'),
               'device': ('Seleccione el dispositivo que presenta inconvenientes'),
               'ip_direction':('Si no existe la direccion ip, agreguela primero haciendo click en el boton "Agregar nueva direccion IP"'),
               'last_revision': ('Ingrese un fecha con el formato DD-MM-AAAA'),
               'tech_revision':('Seleccione el técnico a cargo de la última revision'),
               'office':('Seleccione la oficina en la que se encuentra actualmente el dispositivo'),
          }
          widgets = {

               'dev_type': forms.Select(attrs={
                    'class': 'form-control', 
                    'id':'dev_type',
               }),

               'brand':forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'brand',
               }), 

               'model': forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'dev_model',
               }), 

               'ip_direction': forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'device_ip',
               }),

               'tech_revision': forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'tech_revision',
               }),

               'user': forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'user_device',
               }),
               
               'office': forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'office_device',
               }),
          }     
from django.contrib import admin
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from .validators import MaxSizeFileValidator
from ckeditor.widgets import CKEditorWidget


class HomeForm(forms.ModelForm):
     
     class Meta:
          model = Pendings
          fields = ['required_by', 'personal', 'service_for', 'device', 'reason']
          labels = {
               'required_by': ('Requerido por'),
               'service_for': ('Servicio para'),
               'device': ('Dispositivo'),
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
          }     

#* Device Type Form
class DevTypeFormAdd(forms.ModelForm):
     
     def clean_model(self):
          dev_type = self.cleaned_data['dev_type']
          is_in = DevType.objects.filter(dev_type__iexact=dev_type).exists()

          if is_in:
               raise ValidationError('Este tipo de dispositivo ya se encuentra en la Base de Datos')
          return dev_type

     class Meta:
          model = DevType
          
          fields = '__all__'
          
          labels = {
               'dev_type': ('Tipo de Dispositivo: ')
          }
          help_texts = {
               'dev_type': ('Ingrese un tipo de dispositivo (N° de caracteres máximo = 12)')
          }

          widgets = {
               'dev_type': forms.TextInput(attrs={    
                    'class': 'form-control',       
               })
          }
          

#* Brand Form
class BrandFormAdd(forms.ModelForm):
     
     def clean_model(self):
          model = self.cleaned_data['brand']
          is_in = Brand.objects.filter(brand__iexact=model).exists()

          if is_in:
               raise ValidationError('Esta marca ya se encuentra en la Base de Datos')

          return model

     class Meta:
          model = Brand
          
          fields = '__all__'
          
          labels = {
               'brand': ('Marca de Dispositivo: ')
          }
          
          help_texts = {
               'brand': ('Ingrese una marca (N° de caracteres máximo = 15)')
          }

          widgets = {
               'brand': forms.TextInput(attrs={    
                    'class': 'form-control',       
               })
          }

#* Device Models Form
class DevModelFormAdd(forms.ModelForm):

     def clean_model(self):
          model = self.cleaned_data['model']
          is_in = Model.objects.filter(model__iexact=model).exists()

          if is_in:
               raise ValidationError('Este modelo ya se encuentra en la Base de Datos')

          return model

     img = forms.ImageField(label="", required=True, validators=[MaxSizeFileValidator(max_file_size=5)])
     class Meta:
          model = Model
          
          fields = '__all__'
          
          labels = {
               'img': (''),
               'model': ('Modelo de Dispositivo: ')
          }
          help_texts = {
               'model': ('Ingrese un modelo (N° de caracteres máximo = 11)')
          }

#* Internet Access Form
class InternetAccessAddForm(forms.ModelForm):
     
     def clean_model(self):
          model = self.cleaned_data['access_type']
          is_in = Internet.objects.filter(access_type__iexact=model).exists()

          if is_in:
               raise ValidationError('Esta tipo de acceso ya se encuentra en la Base de Datos')

          return model

     class Meta: 
          model = Internet
          
          fields = '__all__'

          labeles = {
               'access_type': ('Tipo de acceso a internet: ')
          }

          help_texts = {
               'access_type': ('maximo 12 carcateres')
          }

          widgets = {
               'access_type': forms.TextInput(attrs={
                    'class': 'form-control',
               })
          }

#! Ip Add Form
class IpAddForm(forms.ModelForm):
     
     def clean_model(self):
          model = self.cleaned_data['Ip']
          is_in = Ip.objects.filter(ip__iexact=model).exists()

          if is_in:
               raise ValidationError('Esta direccion Ip ya se encuentra registrada en la Base de Datos')

          return model
     
     class Meta:
          model = Ip

          fields = '__all__'
          
          labels = {
               'ipdir':('Direccion Ip: '),
               'internet_access':('Tipo de Acceso a Internet')
          }

          help_texts = {
               'ipdir':('Ingrese la direccion IP segun ejemplo: 192.168.1.1 o 192.168.201.101')
          }

          widgets = {
               'ipdir': forms.TextInput(attrs={
                    'class': 'form-control'
               }),

               'internet_access': forms.Select(attrs={
                    'class': 'form-control', 
                    'placeholder': 'Seleccione un tipo de acceso'

               })
          }


# User Form
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
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
     
     def clean_dev_type(self):
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
     
     def clean_brand(self):
          brand = self.cleaned_data['brand']
          is_in = Brand.objects.filter(brand__iexact=brand).exists()

          if is_in:
               raise ValidationError('Esta marca ya se encuentra en la Base de Datos')

          return brand

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
     
     def clean_access_type(self):
          access_type = self.cleaned_data['access_type']
          is_in = Internet.objects.filter(access_type__iexact=access_type).exists()

          if is_in:
               raise ValidationError('Esta tipo de acceso ya se encuentra en la Base de Datos')

          return access_type

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

#* Ip Add Form
class IpAddForm(forms.ModelForm):
     
     def clean_ipdir(self):
          ipdir = self.cleaned_data['ipdir']
          is_in = Ip.objects.filter(ipdir__iexact=ipdir).exists()

          if is_in:
               raise ValidationError('Esta direccion Ip ya se encuentra registrada en la Base de Datos')

          return ipdir
     
     class Meta:
          model = Ip

          fields = '__all__'
          
          labels = {
               'ipdir':('Direccion Ip: '),
               'internet_access':('Tipo de Acceso a Internet: ')
          }

          help_texts = {
               'ipdir':('Ingrese la direccion IP segun ejemplo: 192.168.1.1 o 192.168.201.101')
          }

          widgets = {
               'ipdir': forms.TextInput(attrs={
                    'class': 'form-control'
               }),

               'internet_access': forms.Select(attrs={
                    'class': 'form-control'
               })
          }

#* Location Add Form
class LocationAddForm(forms.ModelForm):
     
     def clean_location(self):
          location = self.cleaned_data['location']
          is_in = Location.objects.filter(location__iexact=location).exists()

          if is_in:
               raise ValidationError('Esta localidad ya se encuentra agregada a la base de datos')
               
          return location

          
     class Meta:
          model = Location
          
          fields = '__all__'

          labels = {
               'location': ('Nueva Localidad: ')
          }

          help_texts = {
               'location':('Ingrese el nombre de una localidad (Máximo 12 caracteres)')
          }

          widgets = {
               'location': forms.TextInput(attrs={
                    'class': 'form-control'
               })
          }

#* Ediffices Add Form
class EdifficeAddForm(forms.ModelForm):
     def clean_ediffice(self):
          ediffice = self.cleaned_data['ediffice']
          is_in = Edifice.objects.filter(ediffice__iexact=ediffice).exists()

          if is_in:
               raise ValidationError('El edificio ya se encuentra agregado a la base de datos')

          return ediffice

     class Meta:
          model = Edifice

          fields = '__all__'

          labels = {
               'edifice': ('Domicilio/Edificio: ')
          }

          help_texts = {
               'edifice': ('Ingrese un domiicilio o el nombre de un edificio que sea identificable (Máximo 30 caracteres)')

          }

          widgets = {
               'edifice': forms.TextInput(attrs={
                    'class': 'form-control'
               })
          }


#* Office Form
class OfficeFormAdd(forms.ModelForm):

     class Meta:
          model = Office

          fields = '__all__'

          labels = {
               'location': ('Localidad: '),
               'edifice': ('Edificio: '),
               'floor': ('Piso: '),
               'court': ('Juzgado'),
               'office_name': ('Nombre de la Oficina: '),
               'phone_1': ('Telefono 1: '),
               'phone_2': ('Telefono 2: '),
               'phone_3': ('Telefono 3: ')

          }
          help_texts = {
               'office_name': ('Ingrese el nombre de la Secretaria o division (Máximo 50 caracteres) '),
               'phone_1': ('No agregar codigo de area (ej. 4212444)'),
               'phone_2': ('No agregar codigo de area (ej. 4212444)'),
               'phone_3': ('No agregar codigo de area (ej. 4212444)')

          }
          widgets = {

               'location': forms.Select(attrs={
                    'class': 'form-control', 
                    'id':'location',
               }),

               'edifice':forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'edifice',
               }), 

               'floor': forms.TextInput(attrs={
                    'class': 'form-control',
                    'id': 'floor',
               }), 

               'court': forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'court',
               }),

               'office_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'id': 'office_name',
               }),

               'phone_1': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'id': 'phone_1',
               }),

               'phone_2': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'id': 'phone_2',
               }),
               
               'phone_3': forms.NumberInput(attrs={
                    'class': 'form-control', 
                    'id': 'phone_3',
               })
          }



#* User Form
class CustomUserCreationForm(UserCreationForm):
     
     class Meta:
          
          user = User
          
          fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


#* Device Form
class DeviceFormAdd(forms.ModelForm):

     def clean_dev_name(self):
          dev_name = self.cleaned_data['dev_name']
          is_in = Device.objects.filter(device__iexact=dev_name).exists()

          if is_in:
               raise ValidationError('Este modelo ya se encuentra en la Base de Datos')

          return dev_name

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
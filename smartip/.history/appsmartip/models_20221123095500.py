from django.db import models

# Create your models here.

class Brand(models.Model):
     brand = models.CharField(max_length=15)

class Model(models.Model):
     model = models.CharField(max_length=10)

class DevType(models.Model):
     img = models.ImageField()
     dev_type = models.CharField(max_length=10)
     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
     model = models.ForeignKey(Model, on_delete=models.CASCADE)

class Internet(models.Model):
     access_type = models.CharField(max_length=12)

class Location(models.Model):
     location = models.CharField(max_length=8)

class Court (models.Model):
     court = models.CharField(max_length=30)

class Edifice (models.Model):
     edifice = models.CharField(max_length=20)

class Office(models.Model):
     location = models.ForeignKey(Location, on_delete=models.CASCADE)
     edifice = models.ForeignKey(Edifice, on_delete=models.CASCADE)
     floor = models.CharField(max_length=4)
     court = models.ForeignKey(Court, on_delete=models.CASCADE)
     office_name = models.CharField(max_length=25)
     phone_1 = models.IntegerField()
     phone_2 = models.IntegerField()
     phone_3 = models.IntegerField()

class DevUsers(models.Model):
     name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     email = models.CharField(max_length=60)
     message_acount = models.CharField(max_length=15)
     message_pass = models.CharField(max_length=15)
     username = models.CharField(max_length=6)
     standard_password = models.BooleanField()

class Ip (models.Model):
     ipdir = models.CharField(max_length=15)
     internet_access = models.ForeignKey(Internet, on_delete=models.CASCADE)

class Tech (models.Model):
     name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)

class Status (models.Model):
     status = models.CharField(max_length=15)

class Device(models.Model):
     dev_type = models.ForeignKey(DevType, on_delete=models.CASCADE)
     is_active = models.BooleanField()
     is_working = models.BooleanField()
     ip_direction = models.ForeignKey(Ip, on_delete=models.CASCADE)
     last_revision = models.DateField()
     cause = models.CharField(max_length=50)
     tech_revision = models.ForeignKey(Tech, on_delete=models.CASCADE)
     has_user = models.BooleanField()
     user = models.ForeignKey(DevUsers, on_delete=models.CASCADE)
     office = models.ForeignKey(Office, on_delete=models.CASCADE)

class PendStatus():
     status = models.CharField(max_length=15)

class Pendings(models.Model):
     date = models.DateField()
     required_by = models.ForeignKey(DevUsers, on_delete=models.CASCADE)
     office = models.ForeignKey(Office, on_delete=models.CASCADE)
     device = models.ForeignKey(Device, on_delete=models.CASCADE)
     reason = models.TextField()
     status = models.ForeignKey(PendStatus, on_delete=models.CASCADE)

class AssignedTech():
     pending = models.ForeignKey(Pendings, on_delete = models.CASCADE)
     tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
     finihed = models.BooleanField()
     date = models.DateField()
     observations = models.TextField()
     repair = models.CharField(max_length=50)
     status = models.ForeignKey(PendStatus, on_delete=models.CASCADE)

#!Verificar con bibliotecas de Djandgo
# class SystemUsers(models.Model):





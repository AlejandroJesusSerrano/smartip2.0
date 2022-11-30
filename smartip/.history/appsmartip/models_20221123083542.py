from django.db import models

# Create your models here.

class DevType(models.Model):
     type = models.CharField(max_length=10)

class Location(models.Model):
     location = models.CharField(max_length=8)

class Court (models.Model):
     court = models.CharField(max_length=30)

class Edifice (models.Model):
     edifice = models.CharField(max_length=20)



class Office(models.Model):
     office_name = models.CharField(max_length=25)
     court = models.ForeignKey(Court, on_delete=models.CASCADE)
     location = models.ForeignKey(Location, on_delete=models.CASCADE)
     edifice = models.ForeignKey(Edifice, on_delete=models.CASCADE)
     floor = models.CharField(max_length=4)
     phone = models.IntegerField()

class DevUsers(models.Model):
     name = models.CharField(max_lengtn=30)
     last_name = models.CharField(max_length=30)
     username = models.CharField(max_length=6)
     standard_password = models.BooleanField()


#!Verificar con bibliotecas de Djandgo
# class SystemUsers(models.Model):





class Device(models.Model):
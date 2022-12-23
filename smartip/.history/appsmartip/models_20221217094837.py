from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Brand(models.Model):
     brand = models.CharField(max_length=15)

     def __str__(self):
          return self.brand

class DevType(models.Model):
     dev_type = models.CharField(max_length=12)

     def __str__(self):
          return self.dev_type

class Model(models.Model):
     img = models.ImageField(upload_to="devices", null=True)
     model = models.CharField(max_length=11)

     def __str__(self):
          return self.model

class Internet(models.Model):
     access_type = models.CharField(max_length=12)

     def __str__(self):
          return self.access_type
          
class Location(models.Model):
     location = models.CharField(max_length=8)

     def __str__(self):
          return self.location

class Court (models.Model):
     court = models.CharField(max_length=30)

     def __str__(self):
          return self.court
class Edifice (models.Model):
     edifice = models.CharField(max_length=20)

     def __str__(self):
          return self.edifice

class Office(models.Model):
     location = models.ForeignKey(Location, on_delete=models.CASCADE)
     edifice = models.ForeignKey(Edifice, on_delete=models.CASCADE)
     floor = models.CharField(max_length=4)
     court = models.ForeignKey(Court, on_delete=models.CASCADE)
     office_name = models.CharField(max_length=25)
     phone_1 = models.IntegerField(null=True, blank=True)
     phone_2 = models.IntegerField(null=True, blank=True)
     phone_3 = models.IntegerField(null=True, blank=True)

     def __str__(self):
          return self.office_name

class DevUsers(models.Model):
     name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     email = models.CharField(max_length=60)
     message_acount = models.CharField(max_length=15)
     message_pass = models.CharField(max_length=15)
     username = models.CharField(max_length=6)
     standard_password = models.BooleanField()

     def __str__(self):
          return self.username

class Ip (models.Model):
     ipdir = models.CharField(max_length=15)
     internet_access = models.ForeignKey(Internet, on_delete=models.CASCADE)

     def __str__(self):
          return self.ipdir

class Tech (models.Model):
     name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)

     def __str__(self):
          return self.name

class DevStatus (models.Model):
     status = models.CharField(max_length=15)

     def __str__(self):
          return self.status

class Device(models.Model):
     dev_name = models.CharField(max_length=20)
     dev_type = models.ForeignKey(DevType, on_delete=models.CASCADE)
     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
     model = models.ForeignKey(Model, on_delete=models.CASCADE)
     is_working = models.BooleanField()
     is_active = models.BooleanField()
     ip_direction = models.ForeignKey(Ip, on_delete=models.CASCADE)
     last_revision = models.DateField(auto_now=False)
     cause = models.CharField(max_length=50)
     tech_revision = models.ForeignKey(Tech, on_delete=models.CASCADE)
     has_user = models.BooleanField()
     user = models.ForeignKey(DevUsers, on_delete=models.CASCADE)
     office = models.ForeignKey(Office, on_delete=models.CASCADE)

     def __str__(self):
          return self.dev_name

class PendingStatus(models.Model):
     status = models.CharField(max_length=19)

     def __str__(self):
          return self.status

class Pendings(models.Model):
     date = models.DateTimeField(auto_now_add=True)
     required_by = models.ForeignKey(DevUsers, related_name='user_require', on_delete=models.CASCADE)
     personal = models.BooleanField()
     service_for = models.ForeignKey(DevUsers, related_name='user_for', on_delete=models.CASCADE)
     device = models.ForeignKey(Device, on_delete=models.CASCADE)
     reason = RichTextField()
     state = models.ForeignKey(PendingStatus, default=1, on_delete=models.CASCADE)
     updated = models.DateField(auto_now=True)

     def __str__(self):
          return self.reason

class AssignedTech(models.Model):
     assign_date = models.DateTimeField(auto_now_add=True)
     pending = models.ForeignKey(Pendings, on_delete = models.CASCADE)
     tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
     finished = models.BooleanField()
     date = models.DateField()
     observations = models.TextField()
     repair = models.CharField(max_length=50)
     status = models.ForeignKey(PendingStatus, on_delete=models.CASCADE)
     updated = models.DateField(auto_now=True)

     def __str__(self):
          return self.tech






from .models import *
from rest_framework import serializers

class ModelSerializer (serializers.ModelSerializer):
     class Meta:
          model = Model
          fields = '__all__'
          

class PendingSerializer (serializers.ModelSerializer):
     class Meta:
          model = Pendings
          fields = '__all__'
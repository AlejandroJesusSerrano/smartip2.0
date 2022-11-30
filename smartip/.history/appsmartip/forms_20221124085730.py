from django import forms
from .models import *


class HomeForm(forms.Form):

     class Meta:
          model = Pendings
          fields = ['required_by', 'personal', 'name_to_request', 'last_name_to_request', 'device', 'reason']


from django.contrib import admin
from .models import *
from .forms import DevModelFormAdd

# Register your models here.

class ModelAdmin(admin.ModelAdmin):
     form = DevModelFormAdd


admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(DevType)
admin.site.register(Internet)
admin.site.register(Location)
admin.site.register(Court)
admin.site.register(Edifice)
admin.site.register(Office)
admin.site.register(DevUsers)
admin.site.register(Ip)
admin.site.register(Tech)
admin.site.register(DevStatus)
admin.site.register(PendingStatus)
admin.site.register(Device)
admin.site.register(Pendings)



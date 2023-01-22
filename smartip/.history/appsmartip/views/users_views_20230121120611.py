from django.shortcuts import render, redirect, get_object_or_404
from ..models import DevUsers
from ..forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from rest_framework import viewsets
from ..serializers import ModelSerializer
from django.db.models import Q
from ..functions import flag_dev


# * Device Users list
@permission_required('appsmartip.view_dev_users')
def admin_db_offices(request):

    dev_users = DevUsers.objects.all()
    search_du = request.GET.get('search_dev_user')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(dev_users, 10)
        dev_users = paginator.page(page)
    except:
        raise Http404

    if search_du:
        dev_users = DevUsers.objects.filter(
            Q(name__icontains=search_du) |
            Q(last_name__icontains=search_du) |
            Q(email__icontains=search_du) |
            Q(message_account__icontains=search_du) |
            Q(message_pass__icontains=search_du) |
            Q(username__icontains=search_du) 
        ).distinct()

    data = {
        'entity': dev_users,
        'paginator': paginator
    }
    return render(request, 'appsmartip/admin_db/offices/offices.html', data)

# * Office Details
@permission_required('appsmartip.view_office')
def office_details(request, id):
    office = get_object_or_404(Office, id=id)
    device = Device.objects.all()

    devices_office = device.filter(office_id=office.id)

    flag = flag_dev(devices_office)

    data = {
        'office': office,
        'device_office': devices_office,
        'flag': flag
    }

    return render(request, 'appsmartip/admin_db/offices/offices_details.html', data)

# * CRUD
# * Office Add


@permission_required('appsmartip.add_office')
def offices_add(request):
    data = {
        'office_add': OfficeFormAdd()
    }

    if request.method == 'POST':
        offices_add_form = OfficeFormAdd(data=request.POST)

        if offices_add_form.is_valid():
            offices_add_form.save()
            messages.success(request, 'Oficina agregada correctamente')
            return redirect(to='Offices')
        else:
            data['office_add'] = offices_add_form

    return render(request, 'appsmartip/admin_db/offices/offices_add.html', data)

# * Office Edit


@permission_required('appsmartip.modify_office')
def offices_edit(request, id):
    office = get_object_or_404(Office, id=id)
    data = {
        'office_edit_form': OfficeFormAdd(instance=office)
    }

    if request.method == 'POST':
        office_edit = OfficeFormAdd(request.POST, instance=office)

        if office_edit.is_valid():
            office_edit.save()
            messages.success(request, 'La oficina se ha editado correctamente')
            return redirect(to='Offices')
        else:
            data['office_edit_form'] = office_edit

    return render(request, 'appsmartip/admin_db/offices/offices_edit.html', data)


# * Office Delete
permission_required('appsmartip.delelte_office')


def office_delete(request, id):
    office = get_object_or_404(Office, id=id)
    office.delete()
    messages.success(request, 'Oficina eliminada correctamente')
    return redirect(to='Offices')

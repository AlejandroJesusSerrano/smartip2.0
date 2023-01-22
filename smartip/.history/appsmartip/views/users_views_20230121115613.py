from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from ..forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from rest_framework import viewsets
from ..serializers import ModelSerializer
from django.db.models import Q
from ..functions import flag_dev
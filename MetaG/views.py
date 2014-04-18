from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django import forms
from django.http import HttpResponse

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from Pmanager.models import Project

import os

# Create your views here.
# @login_required
def home(request):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_dir = os.path.join(base_dir, 'texts')
    site_title_file = os.path.join(file_dir, 'site_title')
    stf = open(site_title_file, 'r')
    site_desc_file = os.path.join(file_dir, 'site_desc')
    sdf = open(site_desc_file, 'r')
    site_title=stf.read()
    stf.close()
    site_desc=sdf.read()
    sdf.close()
    return render(request, 'home.html', {'sitetitle': site_title, 'description': site_desc})
#    projects = Project.objects.filter(owner__id = request.user.id)
#    return HttpResponse("Hello, %s (%d)" % (request.user.username, request.user.id) )

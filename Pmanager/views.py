from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from Pmanager.models import Project, SequenceFile

from django.shortcuts import render_to_response
from .forms import UploadFileForm, CreateProjectForm, EditProjectForm

import os

# Create your views here.
@login_required
def user_projects(request):
    #    return render(request, 'user_projects.html', {'projecd_ID': project})
    p = Project.objects.filter(owner__id = request.user.id)
    return render( request, 'user_projects.html', {'project': p} )

@sensitive_post_parameters()
@csrf_protect
@never_cache
@login_required
def create_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            p = Project.objects.create(name = name, owner_id = request.user.id)
            p.save()
            return HttpResponseRedirect(reverse('upload_js', args=(p.id,)))
    else:
        form = CreateProjectForm()
    return render(request, 'project_create.html', {
        'form': form,
    })

@sensitive_post_parameters()
@csrf_protect
@never_cache
@login_required
def edit_project(request, id):
    p = get_object_or_404(Project.objects.filter(pk=id, owner__id=request.user.id))
    pp = Project.objects.get(pk=id)
    if request.method == 'POST':
        form = EditProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['new_name']
            pp.name = name
            pp.save()
            return HttpResponseRedirect(reverse('projects'))

    else:
        form = EditProjectForm()
    return render(request, 'project_edit.html', {'form': form, 'project': pp, })

@login_required
def del_project(request, id):
    p = get_object_or_404(Project.objects.filter(pk=id, owner__id=request.user.id))
    pp = Project.objects.get(pk=id)
    if request.method == 'POST':
        pp.delete()
        return HttpResponseRedirect(reverse('projects'))
    return HttpRequest()

def handle_uploaded_file(f,id):
    """
    Projekti uploadi handler (ühekaupa)
    ToDo:
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_dir = os.path.join(base_dir, 'files')
    project_file_dir = os.path.join(file_dir, id)
    os.makedirs(project_file_dir, exist_ok=True)
    out_file = os.path.join(project_file_dir, f.name)
    with open(out_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return str(out_file)

@sensitive_post_parameters()
@csrf_protect
@never_cache
@login_required
def upload_file(request,id):
    """
    Projekti upload
        ToDo:
        lisa SequenceFile-sse uus kirje faili kohta
        muuta 2 faili (oligo ja sff) jaoks
        kirjuta response asemel redirect Run-i konfimiseks (preflight, lipud, kommendid)
    """
    p = get_object_or_404(Project.objects.filter(pk=id, owner__id=request.user.id)) 
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            kala = handle_uploaded_file(request.FILES['file'], id)
            return HttpResponse('Fail on %s' % [str(request.FILES['file'].name)])
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form, 'project': p})


@sensitive_post_parameters()
@csrf_protect
@never_cache
@login_required
def upload_js_file(request,id):
    p = get_object_or_404(Project.objects.filter(pk=id, owner__id=request.user.id))
    if request.method == 'POST':
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_dir = os.path.join(base_dir, 'files')
        report_file = os.path.join(file_dir, 'request.txt')
        f = open(report_file, 'a+b')
        for jura in request.POST:
            yy = str(request.POST[jura])
            f.write(bytes(jura + ': ' + yy + '\n', 'UTF-8'))

        f.close()
        #return HttpResponse()

    return render(request, 'upload_js.html', {'project': p})

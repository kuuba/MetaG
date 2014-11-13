from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from Pmanager import views

urlpatterns = patterns('',
    url(r'^$', views.user_projects, name='projects'),
    url(r'^create/$', views.create_project, name='crproject'),
    url(r'^upload/(\d+)/$', views.upload_file, name='upload'),
    url(r'^edit/(\d+)/$', views.edit_project, name='edproject'),
    url(r'^del/(\d+)/$', views.del_project, name='delproject'),
)

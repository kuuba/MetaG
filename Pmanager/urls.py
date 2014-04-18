from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from Pmanager import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MetaG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.user_projects, name='projects'),
    url(r'^create/$', views.create_project, name='crproject'),
#    url(r'^upload/(\d+)/$', views.upload_js_file, name='upload_js'),
#    url(r'^upload/(\d+)/$', views.upload_file, name='upload'),
    url(r'^upload/(\d+)/$', views.resumable, name='resumable'),
    url(r'^edit/(\d+)/$', views.edit_project, name='edproject'),
    url(r'^del/(\d+)/$', views.del_project, name='delproject'),
)

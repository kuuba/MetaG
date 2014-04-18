from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from Umanager import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'MetaG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create/$', views.user_create, name='create'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
)

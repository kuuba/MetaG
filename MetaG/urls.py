from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'MetaG.views.home', name='home'),
    url(r'^favicon/(?P<icon>.+)\.png$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon/%(icon)s.png')),
    url(r'^site_desc$', 'MetaG.views.site_desc'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('Umanager.urls')),
    url(r'^projects/', include('Pmanager.urls')),
    url(r'^upload/', include('fileupload.urls')),
)

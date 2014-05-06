from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'MetaG.views.home', name='home'),
    url(r'^site_desc$', 'MetaG.views.site_desc'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('Umanager.urls')),
    url(r'^projects/', include('Pmanager.urls')),
)

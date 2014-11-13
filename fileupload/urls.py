# encoding: utf-8
from django.conf.urls import patterns, url
from fileupload.views import UploadCreateView, UploadDeleteView, UploadListView
from django.contrib.auth.views import login, logout


urlpatterns = patterns('',
#    url(r'^new/(\d+)/(\d+)/$', UploadCreateView.as_view(), name='upload-new'),
    url(r'^new/(?P<user>\d+)/(?P<project>\d+)/$', UploadCreateView.as_view(), name='upload-new'),
    url(r'^delete/(?P<pk>\d+)$', UploadDeleteView.as_view(), name='upload-delete'),
    url(r'^view/$', UploadListView.as_view(), name='upload-view'),
)

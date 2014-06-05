# encoding: utf-8
from django.views.generic import CreateView, DeleteView, ListView
from .models import Upload
from .response import JSONResponse, response_mimetype
from .serialize import serialize

from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.utils.decorators import method_decorator

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


class UploadCreateView(CreateView):
    model = Upload
    fields = ['file', 'slug']

#    @sensitive_post_parameters()
#    @csrf_protect
#    @never_cache
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UploadCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class UploadDeleteView(DeleteView):
    model = Upload

#    @sensitive_post_parameters()
#    @csrf_protect
#    @never_cache
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class UploadListView(ListView):
    model = Upload

#    @sensitive_post_parameters()
#    @csrf_protect
#    @never_cache
    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

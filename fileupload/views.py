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

from Pmanager.models import Project

class UploadCreateView(CreateView):
    model = Upload
    fields = ['file', 'slug']

    @method_decorator(login_required)
    @method_decorator(never_cache)
    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(UploadCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.project = Project.objects.get(id = self.kwargs['project'])
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

"""
ToDo:
    genereerida viisakas error (404) kui mingi tont üritab võõra id-ga faili kustutada
"""

class UploadDeleteView(DeleteView):
    model = Upload

    @method_decorator(login_required)
    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(UploadDeleteView, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class UploadListView(ListView):
    model = Upload

    @method_decorator(login_required)
    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(UploadListView, self).dispatch(*args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset().filter(owner=self.request.user) ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

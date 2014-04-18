from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import auth
from django import forms
from django.http import HttpResponse, HttpResponseRedirect

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

# Create your views here.

class UserCreateForm(forms.Form):
    """
    ToDo:
    e-maili olemasolekul password-recovery rutiin
    """
    email = forms.EmailField(max_length=30, label='E-mail for username', help_text='Enter Your e-mail address as username.')
    password = forms.CharField(widget=forms.PasswordInput, max_length=100, help_text='Enter Your password here.')
    password_reentry = forms.CharField(widget=forms.PasswordInput,label='Re-enter password', max_length=100, help_text='Re-enter Your password here.')

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        password = cleaned_data.get("password")
        password_reentry = cleaned_data.get("password_reentry")
        email = cleaned_data.get("email")
        if password != password_reentry:
            raise forms.ValidationError("Passwords don't match!")
        user = User.objects.get(email = email)
        if user:
            raise forms.ValidationError("Email already registered! Please use password recovery if You can't recall Your password.")
        return cleaned_data

@sensitive_post_parameters()
@csrf_protect
@never_cache
def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data["email"],
                    email=form.cleaned_data["email"],
                    password=form.cleaned_data["password"])
            user.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = UserCreateForm()

    return render(request, 'user_create.html', {
        'form': form,
    })

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100, help_text='Enter Your e-mail address here.')
    password = forms.CharField(widget=forms.PasswordInput, max_length=100, help_text='Enter Your password here.')

@sensitive_post_parameters()
@csrf_protect
@never_cache
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect("/projects/")
            else:
                # Show an error page
                return HttpResponseRedirect("/loginerror/")
    else:
        form = UserLoginForm()

    return render(request, 'user_login.html', {
        'form': form,
    })

def user_logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

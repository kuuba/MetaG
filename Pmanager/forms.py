from django import forms

class UploadFileForm(forms.Form):
    file  = forms.FileField()

class CreateProjectForm(forms.Form):
    name = forms.CharField(min_length=4,max_length=500,required=True)

class EditProjectForm(forms.Form):
    new_name = forms.CharField(min_length=4,max_length=500,required=False)

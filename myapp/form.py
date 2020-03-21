from django import forms
from django.forms import ModelForm
from .models import ImportExl

class ImportExlForm(forms.ModelForm):
	class Meta:
		model=ImportExl
		fields=('name', 'age')
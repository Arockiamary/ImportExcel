from django import forms
from django.forms import ModelForm
from .models import ContactForm

class ContactModelForm(forms.ModelForm):
	class Meta:
		model=ContactForm
		fields=('from_email', 'subject', 'message',)
    	


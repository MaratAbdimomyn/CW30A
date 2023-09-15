from django import forms
from django.forms import ModelForm
from .models import *

class Form(forms.ModelForm):
    
    class Meta:
        model = Pagani
        fields = ('brand', 'models_name', 'models_year', 'power')
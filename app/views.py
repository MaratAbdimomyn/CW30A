from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import One
from django.urls import reverse, reverse_lazy
from .forms import *

class OneView(ListView):
    model = Pagani
    template_name = 'home.html'
    context_object_name = 'ones'

class OneCreate(CreateView):
    model = Pagani
    template_name = 'create.html'
    success_url = reverse_lazy('home') 
    form_class = Form
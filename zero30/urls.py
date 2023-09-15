from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OneView.as_view(), name='home'),
    path('create', OneCreate.as_view(), name='create')
]
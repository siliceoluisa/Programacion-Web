from django.urls import include, re_path,path 
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_view
from Registro.views import RegistrateView


app_name = 'Registro'
urlpatterns = [
    path('Registro',RegistrateView.as_view(), name = 'registro')
]
  
from django.urls import include, re_path, path

from django.conf import settings 
from . import views
from django.contrib.auth import views as auth_views

from Login.views import LoginClass
from Login.views import LandingClass
from Login.views import DashboardClass

app_name='Login'
urlpatterns=[
    path('', LandingClass.as_view(),name='landing'),
    path('Login/',LoginClass.as_view(), name='login'),
    path('Dashboard/', DashboardClass.as_view(), name='dashboard'),
]
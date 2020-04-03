
from django.urls import include, re_path,path 
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_view
from Dashboard.views import DashboardClass


app_name = 'Dashboard'
urlpatterns = [
    path('Dashboard',DashboardClass.as_view(), name = 'Dashboard'),
    path('logout/', DashboardClass.logout_request, name='logout'),
]
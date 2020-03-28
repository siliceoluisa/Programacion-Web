from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardClass(LoginRequiredMixin,View):
    templates_okidoki = 'Dashboard/Dashboard.html'
    def get (self,request,*args,**kwargs):
        return render(request,self.templates_okidoki,{})
# Create your views here.

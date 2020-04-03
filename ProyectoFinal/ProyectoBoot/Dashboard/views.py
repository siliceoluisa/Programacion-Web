from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout 
from django.shortcuts import redirect

class DashboardClass(LoginRequiredMixin,View):
    templates = 'Dashboard/Dashboard.html'
    def get (self,request,*args,**kwargs):
        return render(request,self.templates,{})
    
    def logout_request(request):
        logout(request)
        return redirect("Login:login")
        
# Create your views here.

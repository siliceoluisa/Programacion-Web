from django.shortcuts import render
from django.views.generic import View
#importar metodo de autotenticaion
from django.contrib.auth import authenticate
from django.shortcuts import redirect

class LandingClass(View):
    templates='Landing/Landing.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.templates,{})

class DashboardClass(View):
    templates = 'Dashboard/Dashboard.html'
    def get(self, request, *args, **kargs ):
        return render(request, self.templates,{})

class LoginClass(View):
    templates = 'Login/login.html'

    def get(self, request, *args, **kargs ):
        return render(request, self.templates,{} )

    def post(self, request, *args, **kargs ):
        user_post = request.POST['user']
        password_post = request.POST['password']

        user_sesion = authenticate(username = user_post, password = password_post)

        if user_sesion is not None:
            return redirect('login:Dashboard')
            
            #return render(request, self.template_ok,{} )
        else:
            self.message = 'usuario o cantraseña incorrecto'


        return render(request, self.templates, self.get_context())


        
    def get_context(self):
        return{
            'error':self.message,
        }

# Create your views here.

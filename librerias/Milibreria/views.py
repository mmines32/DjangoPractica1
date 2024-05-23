from django.shortcuts import render
from django.http import HttpResponse
from .forms import*

def index(request):
    return render(request,'Milibreria/index.html')

def loginusuario(request):
    contexto = {
        'loginusuario_form' : LoginUsuarioForm()
    }
    return render(request,'Milibreria/loginusuario.html', contexto)
   
def administrador(request):
    
    contexto = {
        'administrador_form' : AdministradorForm()
    }
    return render(request,'Milibreria/administrador.html', contexto)



# Create your views here.


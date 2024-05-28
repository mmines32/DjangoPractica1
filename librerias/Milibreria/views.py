from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from .forms import *

import datetime

def index(request):
    return render(request,'Milibreria/index.html')

def loginusuario(request):
    contexto = {}
    if request.method == "GET":
        contexto['loginusuario_form'] = LoginUsuarioForm()
        
    else:
        form = LoginUsuarioForm(request.POST)  #asumo que es un post#
        contexto['loginusuario'] = form  #genero el login con los datos enviados por usuario#
        
        #validaciones
        if form.is_valid():
            print(request.POST)   # es para ver lo que envia el post #
    
            return redirect('index')   # me redirige al index #
    
    
    return render(request,'Milibreria/loginusuario.html', contexto)


   
def administrador(request):
    
    contexto = {
        'administrador_form' : AdministradorForm()
    }
    return render(request,'Milibreria/administrador.html', contexto)



# Create your views here.


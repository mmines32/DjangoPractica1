from django.shortcuts import render, redirect

from .models import Libro
from .forms import RegisterForm, LoginUsuarioForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        return redirect("inicio_autenticado")
    return render(request,'Milibreria/index.html')


def registrar_usuario(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginusuario")
    else:
        form = RegisterForm()
    return render(request, "Milibreria/registro.html", {"form": form})


def login_usuario(request):
    if request.method == "POST":
        form = LoginUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("usuario")
            login(request, usuario)
            return redirect("inicio_autenticado")
    else:
        form = LoginUsuarioForm()
    return render(request, "Milibreria/login.html", {"form": form})

@login_required
def inicio_autenticado(request):
    libros = Libro.objects.all()
    return render(request, "Milibreria/inicio_autenticado.html", {"libros": libros})

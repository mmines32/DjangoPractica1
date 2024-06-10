from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginUsuarioForm
from django.contrib.auth import login

def index(request):
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
            return redirect("index")
    else:
        form = LoginUsuarioForm()
    return render(request, "Milibreria/login.html", {"form": form})

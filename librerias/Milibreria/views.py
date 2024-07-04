from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Libro, DetalleOrden, Usuario, Orden
from .forms import RegisterForm, LoginUsuarioForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import json

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
    detalles_orden = DetalleOrden.objects.filter(orden__usuario=request.user)
    context = {
        "libros": libros,
        "detalles_orden": detalles_orden
    }
    return render(request, "Milibreria/inicio_autenticado.html", context)

@csrf_exempt
def confirmar_compra(request):
    if request.method == "POST":
        carrito = json.loads(request.POST.get("carrito, []"))
        total = request.POST.get("total, 0")
        
        if not carrito:
            return JsonResponse({"success": False, "message": "No hay libros en el carrito."})
        
        for item in carrito:
            libro = Libro.objects.get(titulo=item["titulo"])
            DetalleOrden.objects.create(
                orden=Orden,
                libro=libro,
                cantidad=item["cantidad"],
                precio=item["precio"]
            )
        
        return JsonResponse({"success": True, "message": "La compra ha sido agregada al carrito."})
    
    return JsonResponse({"success": False, "message": "No se pudo confirmar la compra."})

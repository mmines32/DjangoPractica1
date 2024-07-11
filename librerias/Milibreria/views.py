<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime
#------------------------------------------------------------
from django.views.generic.list import ListView
from .models import Producto, Cliente, Compra
from .forms import *




def index(request):
    contexto={}
    return render(request,'Milibreria/index.html', contexto)

    return render(request,'Milibreria/listaCliente.html')



 


# vista con clases  ver listado--------------

class ProductoListado(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'Milibreria/listaProducto.html'
    


def AltaProducto(request):
    contexto = {}
    
    if request.method == "GET":
        formulario = AltaProductoForm()
        
    else: 
        formulario = AltaProductoForm(request.POST)   
                                                                                                                  
        if formulario.is_valid():
           
            formulario.save()
            
            messages.success(request, 'El libro ha sido cargado exitosamente')
            
            return redirect('listaProducto')
        
        
    contexto["formulario"] = formulario
    return render(request, 'Milibreria/altaProducto.html', contexto)


def editar_producto(request, producto_id):
        producto = get_object_or_404(Producto, id=producto_id)
        if request.method == 'POST':
            form = EditarProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('listaProducto')
        else:
            form = EditarProductoForm(instance=producto)    
        
            contexto = {'form':form, 'producto':producto}
            return render(request, 'Milibreria/editarProducto.html', contexto)
            
def eliminar_producto(request, producto_id):
    try:
        producto = get_object_or_404(Producto, id=producto_id)
        producto.delete()
        messages.success(request, 'Libro eliminado exitosamente.')
        return redirect('listaProducto')
    except Producto.DoesNotExist:
        messages.error(request, 'El producto no existe.')
    except Exception as e:
        messages.error(request, f'Ocurrió un error: {e}')
        return redirect('listaProducto')


class ClienteListado(ListView):
    model = Cliente
    context_object_name = 'clientes'
    template_name = 'Milibreria/listaCliente.html'
    

def ClienteAlta(request):
    contexto = {}
    
    if request.method == "GET":
        formulario = AltaClienteForm()
    else: 
        formulario = AltaClienteForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            
            messages.success(request, 'El cliente ha sido registrado exitosamente')
            
            return redirect('listaCliente')
    
    contexto["formulario"] = formulario    
    return render(request, 'Milibreria/altaCliente.html',contexto)



class CompraListado(ListView):
    model = Compra
    context_object_name = 'compras'
    template_name = 'Milibreria/compra.html'
    


def CompraAlta(request):
    contexto = {}
    
    if request.method == "GET":
        formulario = AltaCompraForm()
    else: 
        formulario = AltaCompraForm(request.POST)
        
        if formulario.is_valid():
            messages.success(request, 'La compra ha sido registrada')
            
            return redirect('index')
    
    contexto["formulario"] = formulario    
    return render(request, 'Milibreria/altaCompra.html',contexto)

=======
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
>>>>>>> 4e13c0e6b073d1bfc4bd300e74baa59a923fff79

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

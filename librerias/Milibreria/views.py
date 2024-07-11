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



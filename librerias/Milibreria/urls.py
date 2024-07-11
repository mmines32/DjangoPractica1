from django.urls import path, re_path, include
from .import views

from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    
    path('altaCliente', views.ClienteAlta, name='altaCliente'),
    
    path('listaCliente', views.ClienteListado.as_view(), name='listaCliente'),
    
    path('altaCompra', views.CompraAlta, name='altaCompra'),
     
    path('listaProducto', views.ProductoListado.as_view(), name='listaProducto'),
      
    path('altaProducto', views.AltaProducto, name='altaProducto'),
    
    path('editar/producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    
    path('eliminar/producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
       
]

<<<<<<< HEAD
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
       
=======
from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registrar_usuario, name='registro'),
    path('loginusuario', views.login_usuario, name='loginusuario'),
    path('inicio_autenticado', views.inicio_autenticado, name='inicio_autenticado'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),
    path('confirmar_compra', views.confirmar_compra, name='confirmar_compra'),
>>>>>>> 4e13c0e6b073d1bfc4bd300e74baa59a923fff79
]

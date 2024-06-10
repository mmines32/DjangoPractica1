from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('registro', views.registrar_usuario, name='registro'),
    
    path('loginusuario', views.login_usuario, name='loginusuario'),
    
]



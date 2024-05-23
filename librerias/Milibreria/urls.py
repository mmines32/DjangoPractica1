from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('loginusuario', views.loginusuario, name='loginusuario'),
    
     path('administrador', views.administrador, name='administrador'),
]



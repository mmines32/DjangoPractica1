from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registrar_usuario, name='registro'),
    path('loginusuario', views.login_usuario, name='loginusuario'),
    path('inicio_autenticado', views.inicio_autenticado, name='inicio_autenticado'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),
]



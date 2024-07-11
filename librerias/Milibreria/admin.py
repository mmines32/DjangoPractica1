from django.contrib import admin
from .models import Producto, Cliente, Compra

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Compra)
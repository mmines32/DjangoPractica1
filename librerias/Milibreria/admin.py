from django.contrib import admin
from .models import Libro, LibroStock, Usuario, Orden, DetalleOrden


admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(LibroStock)
admin.site.register(Orden)
admin.site.register(DetalleOrden)


from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="D.N.I", unique=True)
    
    def __str__(self):
        return f"{self.nombre} | {self.apellido} | DNI: {self.dni}"

class Producto(models.Model):
    libro = models.URLField(verbose_name="Libro", null=True)
    stock = models.IntegerField(verbose_name="Stock")
    tipo = models.CharField(max_length=100, verbose_name="Tipo")
    precio = models.IntegerField(verbose_name="Precio")
    
     
    def __str__(self):
        return f"LIBRO: {self.libro} | STOCK: {self.stock} | TIPO: {self.tipo}  | PRECIO: {self.precio}"
   

      
class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=100, verbose_name="Cantidad")
    fecha = models.DateField(verbose_name="Fecha de compra: ")
    
    def __str__(self):
        return f"Producto: {self.producto} | CLIENTE: {self.cliente} | CANTIDAD: {self.cantidad}  | FECHA: {self.fecha}"
      
 
# Create your models here.

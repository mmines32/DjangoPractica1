from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(
        self, email, nombre, apellido, dni, direccion, telefono, password=None
    ):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")

        usuario = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido,
            dni=dni,
            direccion=direccion,
            telefono=telefono,
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(
        self, email, nombre, apellido, dni, direccion, telefono, password=None
    ):
        usuario = self.create_user(
            email,
            nombre=nombre,
            apellido=apellido,
            dni=dni,
            direccion=direccion,
            telefono=telefono,
            password=password,
        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    dni = models.CharField(max_length=8, verbose_name="DNI", unique=True)
    email = models.EmailField(max_length=50, verbose_name="Email", unique=True)
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono", unique=True)
    password = models.CharField(max_length=100, verbose_name="Contraseña", default="")

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre", "apellido", "dni", "direccion", "telefono"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Libro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name="Precio")
    imagen = models.CharField(max_length=100, null=True, verbose_name="Imagen")
    
    def __str__(self):
        return self.titulo
    

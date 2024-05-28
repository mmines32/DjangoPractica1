from django import forms
from django.core.exceptions import ValidationError


class LoginUsuarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.DecimalField(label="D.N.I", required=True)
    
    """
 def clean_nombre(self):
    if not self.cleaned_data["nombre"].isalpha():
        raise ValidationError("Sólo letras")

    return self.cleaned_data["nombre"]
    
def clean_apellido(self):
    if not self.cleaned_data["apellido"].isalpha():
        raise ValidationError("Sólo letras")

    return self.cleaned_data["apellido"]
 
 
def clean(self):
    cleaned_data = super().clean()
    nombre = cleaned_data.get("nombre")
    apellido = cleaned_data.get("apellido")
        
    if nombre == "Carlos" and apellido == "Lopez":
        raise ValidationError("El usuario Carlos Lopez ya existe")
        
    if self.cleaned_data["dni"] < 1000000:
        raise ValidationError("El dni debe tener 8 digitos")

    return self.cleaned_data

"""
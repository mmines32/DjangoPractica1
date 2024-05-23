from django import forms

class LoginUsuarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.DecimalField(label="D.N.I", required=True)
    email = forms.EmailField(label="Email", required=True)
    clave = forms.CharField(widget=forms.PasswordInput(),label="Crear clave", required=True)
    
class AdministradorForm(forms.Form):
    nombre = forms.CharField(label="Usuario", required=True)
    clave = forms.CharField(widget=forms.PasswordInput(),label="Contraseña", required=True)
        
  
      
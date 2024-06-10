from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import Usuario


class RegisterForm(forms.ModelForm):
    confirmar_contrasena = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )
    contrasena = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = [
            "nombre",
            "apellido",
            "dni",
            "email",
            "direccion",
            "telefono",
            "contrasena",
        ]

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get("contrasena")
        confirmar_contrasena = cleaned_data.get("confirmar_contrasena")

        if contrasena and confirmar_contrasena and contrasena != confirmar_contrasena:
            raise ValidationError("Las contraseñas no coinciden")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["contrasena"])
        if commit:
            user.save()
        return user


class LoginUsuarioForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    contrasena = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput, required=True
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        contrasena = self.cleaned_data.get("contrasena")
        usuario = authenticate(username=email, password=contrasena)

        if usuario is None:
            raise forms.ValidationError("Correo electrónico o contraseña incorrectos")

        self.cleaned_data["usuario"] = usuario
        return self.cleaned_data

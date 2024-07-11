from django import forms
from django.core.exceptions import ValidationError
from .models import Producto 
from .models import Cliente
from .models import Compra
    

    
class AltaClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields = '__all__'
                

    
    
class AltaProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields = '__all__'
                

               
class AltaCompraForm(forms.ModelForm):
    class Meta:
        model=Compra
        fields = '__all__'
                
  
class EditarProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields= '__all__'   
    
    
    
    
    
    
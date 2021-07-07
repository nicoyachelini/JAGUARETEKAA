from django import forms
from .models import Producto

#Creamos un Form basado en el Modelo Producto para el CRUD
class FormAgregarProducto(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Producto
        fields = ('producto_titulo', 'producto_categoria', 'producto_imagen', 'producto_descripcion', 'producto_precio')
        widget = {
            # 'producto_titulo' : forms.TextInput(attrs={'class': 'prod-title'}),
            'producto_titulo' : forms.TextInput,
            'producto_categoria' : forms.TextInput,
            'producto_descripcion' : forms.Textarea,
            'producto_precio' : forms.TextInput(attrs={'type':'number'}),
            'producto_imagen' : forms.FileInput(attrs={'name': 'imagen-adjunta'}),
        }
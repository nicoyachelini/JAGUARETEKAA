from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    categoria_nombre = models.CharField(max_length=64, help_text='Ej.: Árbol, Arbusto, etc...')

    #Defino lo que quiero mostrar en admin
    def __str__(self):
        return f"{self.categoria_nombre}"


#Creo el modelo para Productos
class Producto(models.Model):
    producto_categoria = models.ForeignKey(Categoria, on_delete=CASCADE, related_name="producto_categoria")
    producto_titulo = models.CharField(max_length=64, help_text="Ingrese el nombre del producto")
    producto_descripcion = models.TextField(null=True, blank=True, max_length=150)
    producto_precio = models.IntegerField()#tiene que ser float con decimales para sumar los productos
    producto_imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    
    #Definida la realacion para retornar y visualizar nuestro listado de modelos
    def __str__(self):
        return f"#{self.id} - {self.producto_titulo} ({self.producto_categoria}) / Precio: {self.producto_precio}"

#Creo un usuario pero no se si esta bien
class Usuario(models.Model):
    usuario_nombre = models.CharField(max_length=64)
    usuario_productos = models.ManyToManyField(Producto, blank=True, related_name="usuarios")

    def __str__(self):
        return f"{self.usuario_nombre}"

#Creo el carrito donde se guardan los productos relacionados con un usuario
class Carrito(models.Model):
    carrito_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    carrito_producto = models.ManyToManyField(Producto)

    def __str__(self):
        return f"{self.carrito_usuario} {self.carrito_producto}"
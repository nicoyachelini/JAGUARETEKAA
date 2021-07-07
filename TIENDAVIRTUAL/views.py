from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import *
# from .forms import FormAgregarProducto
from .models import Producto, Categoria, Usuario, Carrito
from django.utils import timezone
#importo datetime de django
import datetime
#importo formularios de django
from django import forms

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


# Create your views here.

def index(request):
   if "agregar_al_carrito" not in request.session:
        request.session["agregar_al_carrito"] = []
   return render(request,"tiendaVirtual/index.html", {
      "lista_productos": Producto.objects.all().order_by('-id'),
      "lista_categorias": Categoria.objects.all(),
      "agregar_al_carrito": request.session["agregar_al_carrito"],
   })

def categorias(request):
   return render(request, "tiendaVirtual/categorias.html", {
      "lista_categorias": Categoria.objects.all()
   })

# def filtro_categorias(request, categoria_id):
#     una_categoria = get_object_or_404(Categoria, id=categoria_id)
#     queryset = Producto.objects.all()
#     queryset = queryset.filter(categoria=una_categoria)
#     return render(request,"tiendaVirtual/categorias.html", {
#         "lista_productos": queryset,
#         "listas_categorias": Categoria.objects.all(),
#         "categoria_seleccionada": una_categoria
#     })

def producto(request, producto_id):
   un_producto = Producto.objects.get(id=producto_id)
   return render(request, "tiendaVirtual/producto.html", {
      "producto": Producto.objects.get(id=producto_id),
   })

#Agregar Producto
@permission_required('TIENDAVIRTUAL.add_producto')
def producto_alta(request):
   #Estos pasando datos por medio de un formulario
   if request.method == "POST":
      user = User.objects.get(username=request.user)
      form = FormAgregarProducto(request.POST, files=request.FILES)
      if form.is_valid():
         form.save()
      # return redirect("tiendaVirtual/index.html") 
      return render(request, "tiendaVirtual/index.html", {
         "lista_productos" : Producto.objects.all()
      })
   else:
      form = FormAgregarProducto()
      return render(request, "tiendaVirtual/producto_alta.html", {
         "form": form
      })

#Modificar Producto
@permission_required('TIENDAVIRTUAL.change_producto')
def producto_modificar(request, producto_id):
   
   un_producto = get_object_or_404(Producto, id=producto_id)

   if request.method == "POST":
      form = FormAgregarProducto(request.POST, files=request.FILES, instance=un_producto)
      if form.is_valid():
         form.save()
         # return redirect("tiendaVirtual/index.html") 
         return render(request, "tiendaVirtual/index.html", {
            "lista_productos" : Producto.objects.all(),
            "lista_categorias": Categoria.objects.all(),
            "agregar_al_carrito": request.session["agregar_al_carrito"]
         })
   else:
      #Trae desde la DB y lo transforma
      form = FormAgregarProducto(instance=un_producto)
      return render(request, 'tiendaVirtual/producto_modificar.html', {
         "un_producto" : un_producto,
         "form" : form
      })


#Eliminar Producto
@permission_required('TIENDAVIRTUAL.delete_producto')
def producto_eliminar(request, producto_id):
   un_producto = get_object_or_404(Producto, id=producto_id)
   un_producto.delete()
   return render(request, "tiendaVirtual/index.html", {
      #Contexto
      "lista_productos" : Producto.objects.all()
   })


def sobre_nosotros(request):
   return render (request, "tiendaVirtual/sobre_nosotros.html", {
      "lista_categorias": Categoria.objects.all(),
   })


@login_required
def agregar_al_carrito(request, producto_id):
   un_producto = get_object_or_404(Producto, id=producto_id)
   for id in request.session["agregar_al_carrito"]:
      if id == producto_id:
         #Existe el producto
         return HttpResponseRedirect(reverse("TIENDAVIRTUAL:producto", args=(un_producto.id)))            
   request.session["agregar_al_carrito"] += [producto_id]
   return HttpResponseRedirect(reverse("TIENDAVIRTUAL:producto", args=(un_producto.id)))

def mi_carrito(request):
   return render (request, "tiendaVirtual/mi_carrito.html", {
      "agregar_al_carrito": request.session["agregar_al_carrito"],
   })
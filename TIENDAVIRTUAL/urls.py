from django.urls import path
from . import views

app_name = "TIENDAVIRTUAL"

urlpatterns = [
    path('', views.index, name="index"),
    path('categorias', views.categorias, name="categorias"),
    # path('filtro_categorias/<int:categorias_id>', views.filtro_categorias, name="filtro_categorias"),
    path('sobre_nosotros', views.sobre_nosotros, name="sobre_nosotros"),
    path('mi_carrito', views.mi_carrito, name="mi_carrito"),
    path('<int:producto_id>', views.producto, name="producto"),
    path('producto_alta', views.producto_alta, name="producto_alta"),
    path('producto_modificar/<int:producto_id>', views.producto_modificar, name="producto_modificar"),
    path('producto_eliminar/<int:producto_id>', views.producto_eliminar, name="producto_eliminar"),
    path('agregar_al_carrito/<int:producto_id>', views.agregar_al_carrito, name="agregar_al_carrito"),
    
]
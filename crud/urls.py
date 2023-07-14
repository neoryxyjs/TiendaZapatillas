from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('Lista_Zapatillas/', lista_zapatillas, name='lista_zapatillas'),
    path('Lista_Categorias/', lista_categorias, name='lista_categorias'),
    path('Lista_Marcas/', lista_marcas, name='lista_marcas'),
    path('Nueva_Categoria/', nueva_categoria, name='nueva_categoria'),
    path('Nueva_Marca/', nueva_marca, name='nueva_marca'),
    path('Nueva_Zapatilla/', nueva_zapatilla, name='nueva_zapatilla'),
    path('Eliminar_Zapatilla/<int:idZapatilla>', eliminar_zapatilla, name='eliminar_zapatilla'),
    path('Editar_Zapatilla/<int:idZapatilla>', editar_zapatilla, name='editar_zapatilla'),
    path('Eliminar_Categoria/<int:idCategoria>', eliminar_categoria, name='eliminar_categoria'),
    path('Editar_Categoria/<int:idCategoria>', editar_categoria, name='editar_categoria'),
    path('Eliminar_Marca/<int:idMarca>', eliminar_marca, name='eliminar_marca'),
    path('Editar_Marca/<int:idMarca>', editar_marca, name='editar_marca'),
    path('Comentarios/', lista_comentarios, name='lista_comentarios'),
]
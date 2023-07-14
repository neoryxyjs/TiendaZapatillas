from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('index/', index, name='index'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contactanos/', contactanos, name='contactanos'),
    path('ubicanos/', ubicanos, name='ubicanos'),
    path('clima/', clima, name='clima'),
    path('Lanzamientos/',lanzamientos_recientes, name='lanzamientos_recientes'),
    path('zapatillas/',zapatillas, name='zapatillas'),
    path('zapatilla/<int:id>/',zapatilla, name='zapatilla'),
]
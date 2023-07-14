from django.urls import path
from .views import *

urlpatterns = [
    path('zapatillas/',zapatillas_list),
    path('zapatillas/<int:zapatilla_id>/',zapatilla_detail)
]
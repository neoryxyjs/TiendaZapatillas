from django.shortcuts import render
from crud.models import Zapatilla
from .serializers import ZapatillaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST','DELETE'])
def zapatillas_list(request):
    if request.method == 'GET':
        zapatillas = Zapatilla.objects.all()

        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            zapatillas = zapatillas.filter(nombre__contains=nombre)
        
        marca = request.GET.get('marca', None)
        if marca is not None:
            zapatillas = zapatillas.filter(marca__nombreMarca__contains=marca)
        
        categoria = request.GET.get('categoria', None)
        if categoria is not None:
            zapatillas = zapatillas.filter(categoria__nombreCategoria__contains=categoria)
        
        zapatillas_serializer = ZapatillaSerializer(zapatillas, many=True)
        return Response(zapatillas_serializer.data)

    elif request.method == 'POST':
        zapatilla_data = JSONParser().parse(request)
        zapatilla_serializer = ZapatillaSerializer(data=zapatilla_data)
        if zapatilla_serializer.is_valid():
            zapatilla_serializer.save()
            return JsonResponse(zapatilla_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(zapatilla_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Zapatilla.objects.all().delete()
        return JsonResponse({'message': '{} Zapatillas fueron eliminadas'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT','DELETE'])
def zapatilla_detail(request,zapatilla_id):
    try:
        zapatilla = Zapatilla.objects.get(id=zapatilla_id)
    except:
        return Response({'mensaje':'La zapatilla {} no existe en nuestros registros'.format(zapatilla_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        zapatilla_serializer = ZapatillaSerializer(zapatilla)
        return Response(zapatilla_serializer.data)
    elif request.method == 'PUT':
        zapatilla_data = JSONParser().parse(request)
        zapatilla_serializer = ZapatillaSerializer(zapatilla,data=zapatilla_data)
        if zapatilla_serializer.is_valid():
            zapatilla_serializer.save()
            return JsonResponse(zapatilla_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(zapatilla_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        zapatilla.delete()
        return Response({'mensaje':'La zapatilla {} fue eliminada'.format(zapatilla_id)},status=status.HTTP_204_NO_CONTENT)

from dataclasses import field
from rest_framework import serializers
from crud.models import *

class ZapatillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zapatilla
        fields = '__all__'
        

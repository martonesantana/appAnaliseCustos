from asyncore import read
from rest_framework import fields, serializers
#from custos import models
from apps.contratos import models



class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contratos
        depth = 1
        fields = '__all__'

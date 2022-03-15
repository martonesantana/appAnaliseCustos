from asyncore import read
from rest_framework import fields, serializers
#from custos import models
from apps.orcamento import models



class OrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Orcamento
        depth = 1
        fields = '__all__'

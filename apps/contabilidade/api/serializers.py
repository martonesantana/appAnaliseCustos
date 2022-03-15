from asyncore import read
from rest_framework import fields, serializers
#from custos import models
from apps.contabilidade import models



class FechamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fechamento
        fields = ('ano','jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez')

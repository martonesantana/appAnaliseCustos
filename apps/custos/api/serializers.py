from asyncore import read
from rest_framework import fields, serializers
#from custos import models
from apps.custos import models


class CustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrecoItemCustos
        depth = 10
        fields = '__all__'


class ItemProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemProdutos
        depth = 4
        fields = ('empresa', 'produtos', 'itens',
                  'beneficios', 'provisoes', 'tributos')

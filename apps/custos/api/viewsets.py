from django.db.models.query import Prefetch
from rest_framework import viewsets
from apps.custos import models
from apps.custos.api import serializers


from rest_framework.permissions import IsAuthenticated


class CustoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CustoSerializer

    def get_queryset(self):
        i = models.PrecoItemCustos.objects.all()
        return i


class ItemProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ItemProdutoSerializer

    def get_queryset(self):
        i = models.ItemProdutos.objects.all()
        return i

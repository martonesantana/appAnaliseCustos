from django.db.models.query import Prefetch
from rest_framework import viewsets
from apps.orcamento import models
from apps.orcamento.api import serializers

from rest_framework.permissions import IsAuthenticated


class OrcamentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrcamentoSerializer
    
    def get_queryset(self):
        i = models.Orcamento.objects.all()
        return i


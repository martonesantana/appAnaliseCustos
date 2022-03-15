from django.db.models.query import Prefetch
from rest_framework import viewsets
from apps.contabilidade import models
from apps.contabilidade.api import serializers


from rest_framework.permissions import IsAuthenticated


class FechamentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.FechamentoSerializer

    def get_queryset(self):
        i = models.Fechamento.objects.all()
        return i

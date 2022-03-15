from django.db.models.query import Prefetch
from rest_framework import viewsets
from apps.contratos import models
from apps.contratos.api import serializers


from rest_framework.permissions import IsAuthenticated


class ContratosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ContratoSerializer

    def get_queryset(self):
        i = models.Contratos.objects.all()
        return i

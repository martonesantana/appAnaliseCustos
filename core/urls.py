"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework import routers
from apps.custos.api import viewsets as custosviewsets
from apps.contratos.api import viewsets as contratosviewsets
from apps.orcamento.api import viewsets as orcamentoviewsets
from apps.contabilidade.api import viewsets as contabilidadeviewsets

route = routers.DefaultRouter()

route.register(r'custos', custosviewsets.CustoViewSet, basename="Custos")
route.register(r'itemprodutos', custosviewsets.ItemProdutoViewSet, basename="Itens Produtos")
route.register(r'contratos', contratosviewsets.ContratosViewSet, basename="Contratos")
route.register(r'orcamento', orcamentoviewsets.OrcamentoViewSet, basename="Orçamentos")
route.register(r'fechamento', contabilidadeviewsets.FechamentoViewSet, basename="Fechamento")


urlpatterns = [
    path('', RedirectView.as_view(url='/app/')),
    path('app/', admin.site.urls),
    path('api/', include(route.urls)),
]

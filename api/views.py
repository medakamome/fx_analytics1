# coding: utf-8


import django_filters
from rest_framework import viewsets, filters
from cms.models import BasicData
from .serializer import BasicDataSerializer


class BasicDataViewSet(viewsets.ModelViewSet):
    """"""
    queryset = BasicData.objects.all()
    serializer_class = BasicDataSerializer
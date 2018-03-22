# coding: utf-8

from rest_framework import routers
from .views import BasicDataViewSet


router = routers.DefaultRouter()
router.register(r'basicdata', BasicDataViewSet)

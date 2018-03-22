# coding: utf-8


from rest_framework import serializers
from cms.models import BasicData


class BasicDataSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = BasicData
        fields = ('symbol', 'period', 'high', 'low', 'open', 'close', 'time')
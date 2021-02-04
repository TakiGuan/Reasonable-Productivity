"""
Description: List Serializer
Version: 1
Author: Taki Guan
Date: 2021-02-04 21:05:55
LastEditors: Taki Guan
LastEditTime: 2021-02-04 21:05:58
"""
from rest_framework.serializers import ModelSerializer
from .models import List


class ListSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"

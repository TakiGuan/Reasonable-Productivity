"""
Description: Model Serializer
Version: 1
Author: Taki Guan
Date: 2021-02-03 22:22:15
LastEditors: Taki Guan
LastEditTime: 2021-02-04 22:59:39
"""
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Task


class TaskSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

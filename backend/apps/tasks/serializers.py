"""
Description: Model Serializer
Version: 1
Author: Taki Guan
Date: 2021-02-03 22:22:15
LastEditors: Taki Guan
LastEditTime: 2021-02-03 22:22:17
"""
from rest_framework.serializers import ModelSerializer
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

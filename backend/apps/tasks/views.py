"""
Description: Model View Set
Version: 1
Author: Taki Guan
Date: 2021-02-03 21:40:02
LastEditors: Taki Guan
LastEditTime: 2021-02-03 22:34:13
"""
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

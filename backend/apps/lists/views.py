"""
Description: List View
Version: 1
Author: Taki Guan
Date: 2021-02-04 20:04:10
LastEditors: Taki Guan
LastEditTime: 2021-02-04 21:10:38
"""
from rest_framework.viewsets import ModelViewSet
from .serializers import ListSerializer
from .models import List


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

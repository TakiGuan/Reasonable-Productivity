"""
Description: List View
Version: 1
Author: Taki Guan
Date: 2021-02-04 20:04:10
LastEditors: Taki Guan
LastEditTime: 2021-02-05 19:07:19
"""
from rest_framework.viewsets import ModelViewSet
from .serializers import ListSerializer, ListItemSerializer
from .models import List, ListItem


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListItemViewSet(ModelViewSet):
    queryset = ListItem.objects.all()

    # 这里必须重写get_queryset函数使得filter生效
    def get_queryset(self):
        return ListItem.objects.filter(list=self.kwargs["list_pk"])

    serializer_class = ListItemSerializer

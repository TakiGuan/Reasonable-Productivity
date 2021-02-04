"""
Description: User View
Version: 1
Author: Taki Guan
Date: 2021-02-04 09:56:48
LastEditors: Taki Guan
LastEditTime: 2021-02-04 16:31:04
"""
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""
Description: List Serializer
Version: 1
Author: Taki Guan
Date: 2021-02-04 21:05:55
LastEditors: Taki Guan
LastEditTime: 2021-02-05 13:30:37
"""
from rest_framework.serializers import (
    ModelSerializer,
    # HyperlinkedModelSerializer,
    # PrimaryKeyRelatedField,
)
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

# from django.contrib.auth import get_user_model
from .models import List, ListItem


class ListSerializer(ModelSerializer):
    # user = PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = List
        fields = "__all__"
        # fields = [
        #     "id",
        #     "name",
        #     "description",
        #     "user",
        #     "created_at",
        #     "updated_at",
        # ]


class ListItemSerializer(ModelSerializer):
    # list = PrimaryKeyRelatedField(queryset=List.objects.all())

    class Meta:
        model = ListItem
        fields = "__all__"
        # fields = ["id", "text", "list", "created_at", "updated_at"]

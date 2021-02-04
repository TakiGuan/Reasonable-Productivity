"""
Description: User Serializer
Version: 1
Author: Taki Guan
Date: 2021-02-04 14:57:52
LastEditors: Taki Guan
LastEditTime: 2021-02-04 14:57:56
"""
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
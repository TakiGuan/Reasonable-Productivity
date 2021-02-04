"""
Description: List Model
Version: 1
Author: Taki Guan
Date: 2021-02-04 20:04:10
LastEditors: Taki Guan
LastEditTime: 2021-02-04 20:05:24
"""
from django.db import models
from django.contrib.auth import get_user_model

from ..utils.models import Timestamp


class List(Timestamp, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    # created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

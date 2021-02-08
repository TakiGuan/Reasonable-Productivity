"""
Description: Task Model
Version: 1
Author: Taki Guan
Date: 2021-02-03 21:40:02
LastEditors: Taki Guan
LastEditTime: 2021-02-07 16:59:13
"""
from django.db import models
from django.contrib.auth import get_user_model

from ..utils.models import Timestamp


class Task(Timestamp, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

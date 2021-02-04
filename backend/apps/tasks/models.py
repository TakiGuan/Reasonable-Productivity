"""
Description: Task Model
Version: 1
Author: Taki Guan
Date: 2021-02-03 21:40:02
LastEditors: Taki Guan
LastEditTime: 2021-02-03 22:25:39
"""
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

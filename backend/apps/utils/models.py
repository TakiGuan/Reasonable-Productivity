"""
Description: Utils Models
Version: 1
Author: Taki Guan
Date: 2021-02-04 20:43:57
LastEditors: Taki Guan
LastEditTime: 2021-02-04 20:46:55
"""
from django.db import models


class Timestamp(models.Model):
    """
    作为第三方类引用，需要设置为abstract，不创建数据表

    Parameters:
        models.Model
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

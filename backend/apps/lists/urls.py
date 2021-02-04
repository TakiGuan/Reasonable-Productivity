"""
Description: List URL
Version: 1
Author: Taki Guan
Date: 2021-02-04 20:04:32
LastEditors: Taki Guan
LastEditTime: 2021-02-04 20:04:36
"""
from django.urls import path, include
from rest_framework import routers
from .views import ListViewSet


router = routers.DefaultRouter()
router.register(r"", ListViewSet)

urlpatterns = [path("", include(router.urls))]
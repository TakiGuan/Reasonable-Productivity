"""
Description: URLS
Version: 1
Author: Taki Guan
Date: 2021-02-03 21:52:23
LastEditors: Taki Guan
LastEditTime: 2021-02-03 21:52:26
"""
from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet


router = routers.DefaultRouter()
router.register(r"", TaskViewSet)

urlpatterns = [path("", include(router.urls))]

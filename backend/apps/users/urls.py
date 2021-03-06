"""
Description: User URLs
Version: 1
Author: Taki Guan
Date: 2021-02-04 09:57:19
LastEditors: Taki Guan
LastEditTime: 2021-02-04 09:57:23
"""
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r"", UserViewSet)

urlpatterns = [path("", include(router.urls))]
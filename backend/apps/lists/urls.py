"""
Description: List URL
Version: 1
Author: Taki Guan
Date: 2021-02-04 20:04:32
LastEditors: Taki Guan
LastEditTime: 2021-02-05 19:06:45
"""
from django.urls import path, include
from rest_framework_nested import routers
from .views import ListViewSet, ListItemViewSet


router = routers.SimpleRouter()
router.register(r"", ListViewSet)


lists_router = routers.NestedSimpleRouter(router, r"", lookup="list")
lists_router.register(r"items", ListItemViewSet)


urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(lists_router.urls)),
]

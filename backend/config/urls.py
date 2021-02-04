"""
Description: URL Configuration
Version: 1
Author: Taki Guan
Date: 2021-02-03 21:28:14
LastEditors: Taki Guan
LastEditTime: 2021-02-04 21:04:37
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls")),
    path("tasks/", include("apps.tasks.urls")),
    path("lists/", include("apps.lists.urls")),
]

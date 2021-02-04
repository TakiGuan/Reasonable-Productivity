"""
Description: List Admin
Version: 1
Author: Taki Guan
Date: 2021-02-04 20:04:10
LastEditors: Taki Guan
LastEditTime: 2021-02-04 21:17:15
"""
from django.contrib import admin
from .models import List


class ListAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")


admin.site.register(List, ListAdmin)

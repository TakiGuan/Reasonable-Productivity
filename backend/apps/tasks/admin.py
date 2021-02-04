"""
Description: Task Admin
Version: 1
Author: Taki Guan
Date: 2021-02-03 21:40:02
LastEditors: Taki Guan
LastEditTime: 2021-02-03 23:13:56
"""
from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at", "updated_at")


admin.site.register(Task, TaskAdmin)

"""
Description: User Model extend Base User Model
Version: 1
Author: Taki Guan
Date: 2021-02-04 09:56:48
LastEditors: Taki Guan
LastEditTime: 2021-02-04 10:09:56
"""
from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

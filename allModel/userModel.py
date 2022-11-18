# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
class user(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    usercode = models.CharField(max_length=120)
from django.db import models

class User(models.Model):
    username    = models.CharField(max_length=120, null=False, default="", unique=True)
    email       = models.EmailField(max_length=120, null=False, default="", unique=True)
    password    = models.CharField(max_length=120, null=False, default="")
    role_id     = models.CharField(max_length=120, null=True, default="0")

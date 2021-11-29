from django.db import models

class Permission(models.Model):
    id          = models.IntegerField(null=False, unique=True, primary_key=True)
    name        = models.CharField(max_length=120, null=False, default="", unique=True)
    desc        = models.CharField(max_length=120, null=False, default="")

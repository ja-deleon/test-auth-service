from django.db import models

class Role(models.Model):
    id          = models.IntegerField(blank=True, null=False, unique=True, primary_key=True)
    name        = models.CharField(max_length=120, null=False, default="", unique=True)
    desc        = models.CharField(max_length=120, null=True, default="")
    permissions = models.CharField(max_length=120, null=True, default="0")
from django.db import models

# Create your models here.
class SighModel(models.Model):
    sigh = models.CharField(max_length=500)
    same = models.IntegerField()
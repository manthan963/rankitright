from django.db import models

# Create your models here.

class UserData(models.Model):
    name = models.CharField(blank=False, max_length=100)
    url = models.URLField(max_length = 200)
    phone = models.IntegerField(blank=False, null=False)
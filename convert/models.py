from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.TextField(null=False)
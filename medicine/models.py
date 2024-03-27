from django.db import models

class Medicines(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    required_quantity = models.IntegerField(max_length=10)
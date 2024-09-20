from django.db import models

class carModel(models.Model):
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()

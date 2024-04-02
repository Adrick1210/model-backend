from django.db import models

# Create your models here.
class Model(models.Model):
    model_id = models.IntegerField()
    name = models.CharField(max_length=250)
    series = models.CharField(max_length=250)
    price_us = models.DecimalField(max_digits=10, decimal_places=2)
    price_jp = models.DecimalField(max_digits=10, decimal_places=0)
    release_date = models.DateField()
    box_art = models.CharField(max_length=900)
    grade = models.CharField(max_length=150)
    scale = models.CharField(max_length=150)
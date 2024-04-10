from django.db import models

# Create your models here.
class Ingr(models.Model):
    ingr_name = models.CharField(max_length= 50)
    ingr_quant = models.IntegerField()
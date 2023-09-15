from django.db import models

class One(models.Model):
    brand = models.CharField(max_length=40)
    models_name = models.CharField(max_length=40)

    class Meta:
        abstract = True

class Pagani(One):
    models_year = models.IntegerField()
    power = models.IntegerField()
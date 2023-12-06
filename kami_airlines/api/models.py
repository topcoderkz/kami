from django.db import models


class Airplane(models.Model):
    volume = models.IntegerField() # id
    passenger_assumptions = models.IntegerField()

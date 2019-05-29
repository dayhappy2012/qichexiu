from django.db import models


class CarList(models.Model):
    car_brand = models.CharField(max_length=16)
    car_icon = models.CharField(max_length=256)
    car_model = models.CharField(max_length=128)
    car_quote = models.CharField(max_length=128)

    class Meta:
        db_table = 'carlist'



from django.db import models


class CarUser(models.Model):

    c_username = models.CharField(max_length=16)
    c_phone = models.CharField(max_length=11, null=True)
    c_password = models.CharField(max_length=256)
    c_is_vip = models.BooleanField(default=0)
    c_car = models.IntegerField(null=True)

    class Meta:
        db_table = 'caruser'



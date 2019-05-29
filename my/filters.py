

from rest_framework.fields import FileField

from car.models import CarList


class CarField(FileField):
    CarList.objects.all()
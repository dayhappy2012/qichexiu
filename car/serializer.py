
from rest_framework import serializers

from car.models import CarList


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarList
        fields = "__all__"





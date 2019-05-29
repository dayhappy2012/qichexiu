from django.core import serializers

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import QuerySet

from car.filters import CarField
from car.models import CarList
from car.serializer import CarListSerializer


class CarView(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = CarList.objects.all()
    serializer_class = CarListSerializer
    filter_class = CarField

    def list(self, request, *args, **kwargs):




        return Response(res)



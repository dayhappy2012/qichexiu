

import django_filters


class CarField(django_filters.rest_framework.FilterSet):
    c_status = django_filters.CharFilter(method='filter_car')

    def filter_car(self, queryset, name, value):

        return queryset
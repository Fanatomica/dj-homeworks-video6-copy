from advertisements.models import Advertisement
from django_filters import rest_framework as filters


class AdvertisementFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at']


from rest_framework.viewsets import ModelViewSet

from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle

from advertisements.permissions import IsOwnerOrReadOnly

from advertisements.models import Advertisement

from advertisements.serializers import AdvertisementSerializer

from advertisements.filters import AdvertisementFilter

from django_filters import rest_framework as filters

from django.db.models import Q


class AdvertisementViewSet(ModelViewSet):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filterset_classes = [AdvertisementFilter,]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['creator']


    def get_permissions(self):

        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        else:
            return []


    def get_queryset(self):

        if self.request.user.pk is None:
            queryset = Advertisement.objects.filter(draft=False)
        else:
            queryset = Advertisement.objects.filter(Q(creator=self.request.user) | Q(draft=False))
        return queryset





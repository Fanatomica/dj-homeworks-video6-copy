from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        admins = User.objects.filter(is_staff=True)
        if request.user in admins:
            return True
        elif request.user == obj.creator:
            return True
        return False




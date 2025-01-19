from rest_framework import viewsets

from apps.role.api.serializers import RoleSerializer
from apps.role.models import Role


class RoleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Role instances.
    """

    queryset = Role.objects.all()
    serializer_class = RoleSerializer

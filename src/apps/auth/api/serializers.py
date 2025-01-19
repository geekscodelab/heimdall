from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Permission model.

    This serializer converts Permission model instances to JSON format and vice versa.
    """

    class Meta:
        """
        Meta options for the PermissionSerializer.
        """

        model = Permission
        fields = ("__all__",)

from rest_framework import serializers

from apps.role.models import Role


class RoleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Role model.

    This serializer converts Role model instances to JSON format and vice versa.
    """

    class Meta:
        """
        Meta class to specify the model and fields to be used in the serializer.
        """

        model = Role
        fields = "__all__"

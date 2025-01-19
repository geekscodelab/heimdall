from django.db import models


class Role(models.Model):
    """
    A Django model representing a role with a unique name and an optional description.

    Attributes:
        name (str): The unique name of the role.
        description (str, optional): A brief description of the role.

    """

    name = models.CharField(
        max_length=255,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        """
        Return a string representation of the Role instance.

        Returns:
            str: The name of the role.

        """
        return self.name

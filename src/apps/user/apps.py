from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    Configuration class for the user application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user"

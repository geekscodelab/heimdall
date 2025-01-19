from typing import Any

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.storage import ImageStorage


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.

    Provides methods for creating users and superusers.
    """

    def create(self, username:str, password:str="", **extra_fields:dict[str, Any]) -> Any:
        """
        Create and save a user with the given fields.

        Args:
            username (str): The username for the new user.
            password (str): The password for the new user.
            **extra_fields: Additional fields for the new user.

        Returns:
            User: The newly created user instance.

        """
        if not username:
            msg = _("The given username must be set")
            raise ValueError(msg)
        username = User.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        record = PasswordRecord(user=user, password=user.password)
        record.save()
        return user

    def create_superuser(self, username: str, password: str="") -> Any:
        """
        Create and save a user with the given username, email, and password.
        """
        username = User.normalize_username(username)
        user = self.create(username=username, password=password)
        user.is_superuser = True
        user.force_change_pass = False
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Represents a user in the system.

    Inherits from Django's AbstractUser and adds additional fields and methods as needed.
    """

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    password = models.CharField(
        _("password"),
        max_length=128,
        default="",
        validators=[validate_password])
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts.",
        ),
    )
    is_staff = models.BooleanField(
        verbose_name=_("staff"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts.",
        ),
    )
    force_change_pass = models.BooleanField(
        verbose_name=_("force change password"),
        default=True,
    )
    date_joined = models.DateTimeField(
        verbose_name=_("date joined"),
        auto_now_add=True,
    )
    first_name = models.CharField(
        verbose_name=_("first name"),
        max_length=150,
        default="",
    )
    last_name = models.CharField(
        verbose_name=_("last name"),
        max_length=150,
        default="",
    )
    avatar = models.ImageField(
        verbose_name=_("avatar"),
        upload_to="avatars/",
        storage=ImageStorage(),
        null=True,
    )

    roles = models.ManyToManyField(
        "Role",
        related_name="users",
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ()

    @property
    def full_name(self) -> str:
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    @property
    def short_name(self) -> str:
        """Return the short name for the user."""
        return self.first_name


class PasswordRecordManager(models.Manager):
    """
    Custom manager for the PasswordRecord model.

    Provides additional methods for creating and managing password records.
    """

    def create(self, **kwargs: Any) -> Any:
        """
        Create a new PasswordRecord instance.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            PasswordRecord: The newly created PasswordRecord instance.

        """
        self.objects.all()[:-3].delete()
        return super().create(**kwargs)


class PasswordRecord(models.Model):
    """
    Represents a record of a user's password history.

    Fields:
        user (User): The user to whom this password record belongs.
        password (str): The hashed password.
        date (datetime): The date when the password was set.
    """

    user = models.ForeignKey(
        User,
        related_name="password_records",
        on_delete=models.CASCADE,
        editable=False,
    )

    password = models.CharField(
        verbose_name=_("password hash"),
        max_length=128,
        editable=False,
    )
    date = models.DateTimeField(
        verbose_name=_("date"),
        auto_now_add=True,
        editable=False,
    )

    objects = PasswordRecordManager()

    class Meta:
        """
        Meta options for the PasswordRecord model.
        """

        get_latest_by = "date"
        ordering = ("-date",)

    def __str__(self) -> str:
        """
        Return a string representation of the PasswordRecord instance.

        Returns:
            str: A string containing the username and the date of the password record.

        """
        return f"{self.user.username} - {self.date}"



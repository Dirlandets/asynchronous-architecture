from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # type: ignore
    """App base user."""

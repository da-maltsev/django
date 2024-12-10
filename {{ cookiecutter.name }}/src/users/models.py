from typing import ClassVar

from django.contrib.auth.models import AbstractUser, UserManager as _UserManager


class User(AbstractUser):
    objects: ClassVar[_UserManager] = _UserManager()

from django.db import models
from django.contrib.auth.models import AbstractUser

class UserTypeEnum(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    AUTHOR = "AUTHOR", "Author"
    EUSER = "END_USER", "End_user"

class User(AbstractUser):
    bio = models.CharField(max_length=255, default="", null=True)
    role = models.CharField(max_length=255,choices=UserTypeEnum.choices, default=UserTypeEnum.EUSER)
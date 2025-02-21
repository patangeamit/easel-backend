from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserTypeEnum(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    AUTHOR = "AUTHOR", "Author"
    EUSER = "END_USER", "End_user"
class User(AbstractBaseUser):
    role = models.CharField(max_length=10, choices=UserTypeEnum.choices, default=UserTypeEnum.EUSER)
    bio = models.TextField(blank=True, null=True)
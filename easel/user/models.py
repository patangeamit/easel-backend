from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserTypeEnum(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    AUTHOR = "AUTHOR", "Author"
    EUSER = "END_USER", "End_user"
class User(AbstractBaseUser):
    username = models.CharField(max_length=64)
    role = models.CharField(max_length=10, choices=UserTypeEnum.choices, default=UserTypeEnum.EUSER)
    bio = models.TextField(blank=True, null=True)

    # LOGIN_FIELDS = ['username']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
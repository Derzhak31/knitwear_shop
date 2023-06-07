from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateField(max_length=8, null=True)
    sex = models.CharField(max_length=7)

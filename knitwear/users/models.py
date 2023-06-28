from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SEX_CHOICES = (
        ('m', 'Мужской'),
        ('w', 'Женский'),
    )

    birthday = models.DateField()
    sex = models.CharField(max_length=7, choices=SEX_CHOICES, default='m')


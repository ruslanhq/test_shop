from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Fields 'username' and 'password' inherited from 'AbstractUser'
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    #Abstract User will automatically create a 'password' field
    #Tell Django we want to use the email field as a username for login

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #email, password required by default
from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractUser

class User(BaseModel, AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return self.email

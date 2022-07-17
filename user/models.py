from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  username = models.CharField(max_length = 50, unique = True)
  email = models.EmailField(unique = True)
  education = models.CharField(max_length = 50)
  score = models.PositiveIntegerField(default=0)
  password = models.CharField(max_length = 300)
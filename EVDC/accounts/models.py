from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
  USER_TYPE_CHOICES = (
      ('superAdmin','superAdmin'),
      ('cityAdmin','cityAdmin'),
      ('subcityAdmin','subcityAdmin'),
      ('cityStaff','cityStaff'),
      ('subcityStaff','subcityStaff'),
  )

  Roll = models.CharField(max_length=20,choices=USER_TYPE_CHOICES)
  
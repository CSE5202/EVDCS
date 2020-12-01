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
class Phonenumber(models.Model):
    Phonenumber = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Phonenumber"
        verbose_name_plural = "Phonenumbers"

    def __unicode__(self):
        return self.name
    def __str__(self):
      return self.Phonenumber



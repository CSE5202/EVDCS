from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class users(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	roll = models.CharField(max_length=200)
	created_at = models.DateTimeField('created at')
    def __str__(self):
        return self.username
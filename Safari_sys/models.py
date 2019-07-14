from django.db import models


class AuthInfo(models.Model):
    username = models.CharField(max_length=45, unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)


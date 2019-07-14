from django.db import models


class AuthInfo(models.Model):
    username = models.CharField(max_length=45, unique=True)
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    mail = models.CharField(max_length=100, unique=True)
    p_code = models.CharField(max_length=100)


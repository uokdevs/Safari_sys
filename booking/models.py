from django.db import models
from Safari_sys.models import AuthInfo


# Create your models here.
class BusData(models.Model):
    route_id = models.IntegerField()
    seats_left = models.IntegerField()
    depature = models.TimeField()
    date = models.DateField()
    str_route = models.CharField(max_length=100)


class Booked(models.Model):
    date_booked = models.DateField()
    time_booked = models.TimeField()
    owner = models.ForeignKey(
        AuthInfo,
        on_delete=models.CASCADE
    )
    str_route = models.CharField(max_length=100)

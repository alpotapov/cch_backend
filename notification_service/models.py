from django.db import models


class CCIEntry(models.Model):
    recorded_at = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    MDI_OBD_MILEAGE = models.IntegerField()
    MDI_OBD_FUEL = models.IntegerField()
    GPS_DIR = models.FloatField()
    GPS_SPEED = models.IntegerField()
    IGNITION = models.BooleanField()

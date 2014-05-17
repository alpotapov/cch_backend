from django.db import models


class User(models.Model):
    connected_car_id = models.CharField(max_length=50)
    notification_id = models.CharField(max_length=50)
    tank_max_value = models.FloatField(max_length=50, blank=True, null=True)
    fuel_type = models.IntegerField(max_length=1)  # diesel=0, e10=1, e5=2
    average_fuel_consumption = models.FloatField(max_length=50, blank=True, null=True)
    last_fuel_amount = models.FloatField(max_length=50, blank=True, null=True)


class RefuelEvent(models.Model):
    amount = models.IntegerField(max_length=100)
    user = models.ForeignKey(User)
    longtitude = models.FloatField()
    latitude = models.FloatField()
    gas_station_id = models.IntegerField(max_length=20, blank=True, null=True)
    liked = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)


class Recommendation(models.Model):
    user = models.ForeignKey(User)
    rating = models.FloatField()
    gas_station_id = models.IntegerField(max_length=20)
    longtitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    adress = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(max_length=10)
from restservice.models import User, RefuelEvent, Recommendation
from rest_framework import serializers
from django.forms import widgets


# class UserSerializer(serializers.Serializer):
#     pk = serializers.Field()
#     connected_car_id = serializers.CharField(max_length=50, required=True)
#     notification_id = serializers.CharField(max_length=50, required=True)
#     tank_max_value = serializers.FloatField(required=False)
#     fuel_type = serializers.IntegerField(required=False)  # diesel=0, e10=1, e5=2
#     average_fuel_consumption = serializers.FloatField(required=False)
#     last_fuel_amount = serializers.FloatField(required=False)
#
#     def restore_object(self, attrs, instance=None):
#         if instance:
#             # Update existing instance
#             instance.connected_car_id = attrs.get('connected_car_id', instance.connected_car_id)
#             instance.notification_id = attrs.get('notification_id', instance.notification_id)
#             instance.tank_max_value = attrs.get('tank_max_value', instance.tank_max_value)
#             instance.fuel_type = attrs.get('fuel_type', instance.fuel_type)
#             instance.average_fuel_consumption = attrs.get('average_fuel_consumption', instance.average_fuel_consumption)
#             instance.last_fuel_amount = attrs.get('last_fuel_amount', instance.last_fuel_amount)
#
#         # Create new instance
#         return User(**attrs)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'connected_car_id',
            'notification_id',
            'tank_max_value',
            'fuel_type',
            'average_fuel_consumption',
            'last_fuel_amount'
        )

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.connected_car_id = attrs.get('connected_car_id', instance.connected_car_id)
            instance.notification_id = attrs.get('notification_id', instance.notification_id)
            instance.tank_max_value = attrs.get('tank_max_value', instance.tank_max_value)
            instance.fuel_type = attrs.get('fuel_type', instance.fuel_type)
            instance.average_fuel_consumption = attrs.get('average_fuel_consumption', instance.average_fuel_consumption)
            instance.last_fuel_amount = attrs.get('last_fuel_amount', instance.last_fuel_amount)

        # Create new instance
        return User(**attrs)


class RefuelEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = RefuelEvent
        fields = ('id', 'user', 'longitude', 'latitude', 'gas_station_id', 'liked', 'datetime')

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.user = attrs.get('user', instance.user)
            instance.longitude = attrs.get('longitude', instance.longitude)
            instance.latitude = attrs.get('latitude', instance.latitude)
            instance.gas_station_id = attrs.get('gas_station_id', instance.gas_station_id)
            #instance.liked = attrs.get('liked', instance.liked)
            instance.datetime = attrs.get('datetime', instance.datetime)

        # Create new instance
        return RefuelEvent(**attrs)
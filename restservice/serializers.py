from restservice.models import User, RefuelEvent, Recommendation
from rest_framework import serializers


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
        fields = ('id', 'user', 'amount', 'longitude', 'latitude', 'gas_station_id', 'liked', 'datetime')

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.user = attrs.get('user', instance.user)
            instance.amount = attrs('amount', instance.amount)
            instance.longitude = attrs.get('longitude', instance.longitude)
            instance.latitude = attrs.get('latitude', instance.latitude)
            instance.gas_station_id = attrs.get('gas_station_id', instance.gas_station_id)
            instance.liked = attrs.get('liked', instance.liked)
            instance.datetime = attrs.get('datetime', instance.datetime)

        # Create new instance
        return RefuelEvent(**attrs)


class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = (
            'id',
            'user',
            'rating',
            'gas_station_id',
            'longitude',
            'latitude',
            'name',
            'brand',
            'address',
            'zip_code',
            'city',
            'price'
        )

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.user = attrs.get('user', instance.user)
            instance.rating = attrs.get('rating', instance.rating)
            instance.gas_station_id = attrs.get('gas_station_id', instance.gas_station_id)
            instance.longitude = attrs.get('longitude', instance.longitude)
            instance.latitude = attrs.get('latitude', instance.latitude)
            instance.name = attrs.get('name', instance.name)
            instance.brand = attrs.get('brand', instance.brand)
            instance.address = attrs.get('address', instance.address)
            instance.zip_code = attrs.get('zip_code', instance.zip_code)
            instance.city = attrs.get('city', instance.city)
            instance.price = attrs.get('price', instance.price)
            instance.datetime = attrs.get('datetime', instance.datetime)

        # Create new instance
        return Recommendation(**attrs)
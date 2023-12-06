from rest_framework import serializers
from .models import Airplane
import math


class AirplaneSerializer(serializers.ModelSerializer):
    fuel_consumption = serializers.SerializerMethodField()
    max_minutes_able_to_fly = serializers.SerializerMethodField()

    class Meta:
        model = Airplane
        fields = ['volume', 'passenger_assumptions', 'fuel_consumption', 'max_minutes_able_to_fly']

    def validate_volume(self, value):
        if value <= 0:
            raise serializers.ValidationError("Volume should be more than 0.")
        return value

    def validate_passenger_assumptions(self, value):
        if value < 0:
            raise serializers.ValidationError("Passenger assumptions should be a non-negative integer.")
        return value

    def get_fuel_consumption(self, obj):
        return math.log(obj.volume, 10) * 0.80 + 0.002 * obj.passenger_assumptions

    def get_max_minutes_able_to_fly(self, obj):
        return (200 * obj.volume) / self.get_fuel_consumption(obj)

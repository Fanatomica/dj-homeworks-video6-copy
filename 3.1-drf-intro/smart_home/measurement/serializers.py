from rest_framework import serializers

from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'picture']


class SensorDetailSerializer(serializers.ModelSerializer):
     measurements = MeasurementSerializer(read_only=True, many=True)

     class Meta:
         model = Sensor
         fields = ['id', 'name', 'description', 'measurements']


class MeasurementPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['picture']
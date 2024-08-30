from rest_framework import serializers
from .models import DeviceData

# Create a serializer for the DeviceData model
class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceData
        fields = '__all__'

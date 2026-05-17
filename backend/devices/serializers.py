from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    is_available = serializers.BooleanField(read_only=True)

    class Meta:
        model = Device
        fields = [
            'id',
            'name',
            'serial',
            'device_type',
            'status',
            'location',
            'registered_at',
            'last_seen_at',
            'is_available',
        ]
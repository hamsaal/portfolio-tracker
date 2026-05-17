from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source='device.name', read_only=True)
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = [
            'id',
            'name',
            'device',
            'device_name',
            'status',
            'submitted_by',
            'created_at',
            'started_at',
            'completed_at',
            'duration',
        ]

    def get_duration(self, obj):
        if obj.duration is None:
            return None
        return str(obj.duration)
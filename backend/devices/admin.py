from django.contrib import admin
from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial', 'device_type', 'status', 'location']
    list_filter = ['status', 'device_type']
    search_fields = ['name', 'serial']
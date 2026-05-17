from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'device', 'status', 'submitted_by', 'created_at']
    list_filter = ['status']
    search_fields = ['name', 'submitted_by']
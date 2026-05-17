from django.db import models


class Device(models.Model):

    class Status(models.TextChoices):
        ONLINE   = 'online',   'Online'
        OFFLINE  = 'offline',  'Offline'
        PRINTING = 'printing', 'Printing'
        ERROR    = 'error',    'Error'

    class DeviceType(models.TextChoices):
        FDM   = 'fdm',   'FDM'
        RESIN = 'resin', 'Resin'
        SLS   = 'sls',   'SLS'

    name        = models.CharField(max_length=100)
    serial      = models.CharField(max_length=50, unique=True)
    device_type = models.CharField(max_length=10, choices=DeviceType.choices)
    status      = models.CharField(max_length=10, choices=Status.choices, default=Status.OFFLINE)
    location    = models.CharField(max_length=100, blank=True, default='')
    registered_at = models.DateTimeField(auto_now_add=True)
    last_seen_at  = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.serial})"

    @property
    def is_available(self):
        return self.status == self.Status.ONLINE
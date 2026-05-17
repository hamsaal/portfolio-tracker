from django.db import models
from devices.models import Device


class Job(models.Model):
    class Status(models.TextChoices):
        QUEUED    = 'queued',    'Queued'
        PRINTING  = 'printing',  'Printing'
        COMPLETED = 'completed', 'Completed'
        FAILED    = 'failed',    'Failed'

    device       = models.ForeignKey(Device, on_delete=models.PROTECT, related_name='jobs')
    name         = models.CharField(max_length=100)
    status       = models.CharField(max_length=10, choices=Status.choices, default=Status.QUEUED)
    submitted_by = models.CharField(max_length=100)
    created_at   = models.DateTimeField(auto_now_add=True)
    started_at   = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} on {self.device}"

    @property
    def duration(self):
        if self.completed_at and self.started_at:
            return self.completed_at - self.started_at
        return None
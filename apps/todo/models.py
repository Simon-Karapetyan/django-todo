from django.db import models
from django.utils import timezone


class Todo(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)

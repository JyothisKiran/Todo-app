from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(blank=False, null=False)
    description = models.CharField(blank=False, null=False)

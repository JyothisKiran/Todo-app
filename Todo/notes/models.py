from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name='notes')
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=254, blank=False, null=False)

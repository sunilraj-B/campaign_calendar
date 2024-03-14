from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import timedelta
class Event(models.Model):
    name = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    starting_date = models.DateField()
    week2_date = models.DateField(null=True, blank=True)
    week3_date = models.DateField(null=True, blank=True)
    week4_date = models.DateField(null=True, blank=True)
    
     # Backlog fields
    week2_backlog = models.BooleanField(default=False)
    week3_backlog = models.BooleanField(default=False)
    week4_backlog = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


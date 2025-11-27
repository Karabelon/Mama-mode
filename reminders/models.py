from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_name = models.CharField(max_length=200)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.event_name



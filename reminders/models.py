from django.db import models

class Reminder(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name


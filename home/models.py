from django.db import models

class BabyActivity(models.Model):
    ACTIVITY_TYPES = [
        ('feeding', 'Feeding'),
        ('diaper', 'Diaper Change'),
        ('sleep', 'Sleep'),
        ('bath', 'Bath'),
    ]

    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    time = models.DateTimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} at {self.time}"


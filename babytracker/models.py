from django.db import models
from django.contrib.auth.models import User

class BabyActivity(models.Model):
    ACTIVITY_TYPES = [
        ("feeding", "Feeding"),
        ("sleep", "Sleep"),
        ("diaper", "Diaper Change"),
        ("milestone", "Milestone"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_type


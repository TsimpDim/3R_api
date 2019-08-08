from django.db import models
from django.contrib.auth.models import User

class Option(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    
    SORTING_CHOICES = [
        ('TAS', 'Time Ascending'),
        ('TDE', 'Time Descending'),
        ('AAS', 'Alphab Ascending'),
        ('ADE', 'Alphab Descending'),
        ('NOS', 'No Sorting')
    ]

    sort = models.CharField(max_length=3, choices=SORTING_CHOICES, default='TAS')

    def __str__(self):
        return f"{self.user} - {self.sort}"
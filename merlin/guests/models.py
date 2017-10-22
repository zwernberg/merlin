from django.db import models

# Create your models here.
TRIBE_CHOICES = (
    ('0', 'Wernberg'),
    ('1', 'Larson'),
    ('2', 'Both'),
)

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    attending = models.BooleanField(default=True)
    tribe = models.CharField(max_length=1, choices=TRIBE_CHOICES, default = 2)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

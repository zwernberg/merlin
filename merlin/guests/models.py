from django.db import models

# Create your models here.
TRIBE_CHOICES = (
    ('0', 'Wernberg'),
    ('1', 'Larson'),
    ('2', 'Both'),
)

class HouseHold(models.Model):
    family_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.family_name

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    attending = models.BooleanField(default=True)
    tribe = models.CharField(max_length=1, choices=TRIBE_CHOICES, default = 2)
    household = models.ForeignKey(HouseHold, blank=True, null=True, related_name = 'guests')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

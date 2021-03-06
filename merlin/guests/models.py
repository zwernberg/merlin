from django.db import models

# Create your models here.
TRIBE_CHOICES = (
    ('0', 'Wernberg'),
    ('1', 'Larson'),
    ('2', 'Both'),
    ('3', 'Larson-Wernberg')
)

class HouseHold(models.Model):
    family_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, blank=True)
    save_the_date = models.BooleanField(default=False, verbose_name="Save The Date Sent")
    tribe = models.CharField(max_length=1, choices=TRIBE_CHOICES, default = 1)

    def family_size(self):
        return self.guests.count()

    def has_address(self):
        return not (self.address in [None, ''])
    has_address.boolean = True

    def __str__(self):
        return self.family_name



class Guest(models.Model):
    BOOL_CHOICES = (('0', 'No'), ('1', 'Yes'), ('2', 'Maybe'))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    attending = models.CharField(default=1, choices=BOOL_CHOICES, max_length=1)
    tribe = models.CharField(max_length=1, choices=TRIBE_CHOICES, default = 2)
    household = models.ForeignKey(HouseHold, blank=True, null=True, related_name = 'guests')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

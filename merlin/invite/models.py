from django.db import models

STEAK = 0
SALMON = 1
PENNE = 2
KIDS = 3
NONE = 999
# Create your models here.
FOOD_CHOICES = (
    (STEAK, 'STEAK'),
    (SALMON, 'SALMON'),
    (PENNE, 'PENNE'),
    (KIDS, 'KIDS'),
    (NONE, 'NONE')
)

class RSVP(models.Model):
    name = models.CharField(max_length = 150)
    created = models.DateTimeField(auto_now_add=True)
    attending = models.BooleanField()
    food_choice = models.IntegerField(choices=FOOD_CHOICES, default=NONE)
    song_choice = models.TextField(blank=True)
    message = models.TextField(blank=True)

    def reserved_count(self):
        return 1 + self.guests.count()

    def __str__(self):
        return self.name

class Guest(models.Model):
    rsvp = models.ForeignKey(RSVP, related_name="guests", on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    created = models.DateTimeField(auto_now_add=True)
    food_choice = models.IntegerField(choices=FOOD_CHOICES, default=NONE)

class Decline(models.Model):
    name = models.CharField(max_length = 150)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class RSVP(models.Model):
    name = models.CharField(max_length = 150)
    attending = models.BooleanField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Decline(models.Model):
    name = models.CharField(max_length = 150)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

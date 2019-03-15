from django.db import models

# Create your models here.
class UserData(models.Model):
    crop = models.CharField(
        'Crop',
        max_length=20,
        blank=True, null=True
    )
    bags = models.CharField(
        'Number of bags',
        max_length=20,
        blank=True, null=True
    )
    pickup = models.CharField(
        'Pickup Location',
        max_length=30,
        blank=True, null=True
    )
    destination = models.CharField(
        'Destination',
        max_length=30,
        blank=True, null=True
    )
    mobile_money = models.CharField(
        'Mobile money number',
        max_length=30,
        blank=True, null=True
    )
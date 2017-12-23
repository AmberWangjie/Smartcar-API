from django.db import models
from rest_framework.reverse import reverse
from rest_framework import serializers

#import uuid

# Create your models here.

class Vehicle(models.Model):
    DOOR_COUNT_CHOICES = ((2, 'twoDoorCoupe'), (4, 'fourDoorSedan'))
    
    vid = models.CharField(max_length=100, primary_key=True, blank=False)
    vin = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=100, blank=False)
    doorCount = models.IntegerField(choices=DOOR_COUNT_CHOICES)
    driveTrain = models.CharField(max_length=100, blank=False)


class Security(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='doors', on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    locked = models.BooleanField(default=True,blank=False)


class Fuel(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='fuelLevel', on_delete=models.CASCADE)
    percent = models.FloatField(null=True, blank=True, default=None)

    
class Battery(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='batteryLevel', on_delete=models.CASCADE)
    percent = models.FloatField(null=True, blank=True, default=None)


class Engine(models.Model):
    ACTION_CHOICES = (('START', 'start'), ('STOP', 'stop'))
    STATUS_CHOICES = (('success', 'executed'), ('error', 'failed'))

    vehicle = models.ForeignKey(Vehicle, related_name='engineStatus', on_delete=models.CASCADE)
    action = models.CharField(max_length=100, choices=ACTION_CHOICES)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    #state = models.BooleanField(default=False, null=False)

from pyexpat import model
from django.db import models
from datetime import time

class Bus(models.Model):
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code


class Trip(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    deperture =  models.CharField(max_length=20)
    distinaton =  models.CharField(max_length=20)
    start_time =  models.DateTimeField()
    end_time =   models.DateTimeField()
    watch = models.BooleanField()


    def __str__(self) -> str:
        return f"{self.deperture} - {self.distinaton}"
# Create your models here.

from django.db import models

UserDetails(models.Model):
    title = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100)
    notes = models.CharField(max_length = 100)

    def __str__(self):
        return self.title
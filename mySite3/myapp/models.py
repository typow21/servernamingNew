# Create your models here.

from django.db import models

class Server(models.Model):
    OS = models.CharField(max_length = 100)
    purpose = models.CharField(max_length = 100)
    role = models.CharField(max_length = 100)
    # name = os + purpose + role
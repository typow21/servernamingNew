# Create your models here.

from django.db import models

class UserDetails(models.Model):
    blank = "--"
    linux = "35"
    windows = "30"
    
    web = "20"
    app = "21"
    database = "22"
    storage = "23"
    
    prd = "001"
    np = "100"
    test = "111"
    OS  = (
    (blank,"--"),
    (linux, "Linux/Unix"),
    (windows, "Windows"),
    )
    PURPOSE = (
    (blank,"--"),
    (prd, "prd"),
    (np, "np"),
    (test, "test"),
    )
    ROLE = (
    (blank,"--"),
    (web, "web"),
    (app, "app"),
    (database, "db"),
    (storage, "storage"),
    )

    tu = models.CharField(max_length = 2, default = "tu")
    os = models.CharField(
        max_length = 10,
        choices = OS,
        default = blank,
    )
    purpose = models.CharField(
        max_length = 10,
        choices = PURPOSE,
        default = blank,
    )
    role = models.CharField(
        max_length = 10,
        choices = ROLE,
        default = blank,
    )
    sequence = models.CharField(max_length = 100, default = "000")



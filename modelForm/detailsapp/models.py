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
    
    OpSys  = (
    (blank,"--"),
    (linux, "Linux/Unix"),
    (windows, "Windows"),
    )
    PURPOSE = (
    (blank,"--"),
    (prd, "Production"),
    (np, "Non-Production"),
    (test, "Test"),
    )
    ROLE = (
    (blank,"--"),
    (web, "Web"),
    (app, "Application"),
    (database, "Database"),
    (storage, "Storage"),
    )

    tu = models.CharField(max_length = 2, default = "tu")
    OS = models.CharField(
        max_length = 10,
        choices = OpSys,
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



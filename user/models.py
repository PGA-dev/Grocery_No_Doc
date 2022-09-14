from tkinter import CASCADE
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)


    class Meta:
        verbose_name_plural = "User"

class Budget(models.Model):
    account = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = "Budget"
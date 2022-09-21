import decimal
from sys import maxsize
from django.db import models
from django.utils import timezone

# Create your models here.
class Items(models.Model):
    groc_item = models.CharField(max_length=100)
    notes = models.TextField()
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    item_pprice = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['groc_item']
        verbose_name_plural = "Items"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
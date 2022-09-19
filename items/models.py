from django.db import models
from django.utils import timezone

# Create your models here.
class Items(models.Model):
    groc_item = models.CharField(max_length=70)
    notes = models.TextField()
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    item_pprice = models.DecimalField(max_digits=8, decimal_places=2)
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['groc_item']
        verbose_name_plural = "Items"

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    create_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
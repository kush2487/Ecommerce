from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # stock = models.IntegerField(default=)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f" {self.name} |  {self.price} |  {self.description} "  

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    shelf_location = models.CharField(max_length=100)
    date_entered = models.DateField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)
    amount_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Ensure this field is included

    def __str__(self):
        return self.product_name
    
    
class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_of_sales = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.product.quantity < self.quantity:
            raise ValidationError(f"Cannot sell {self.quantity} units of {self.product.product_name}. Only {self.product.quantity} units available.")
        super().save(*args, **kwargs)
        self.product.quantity -= self.quantity
        self.product.save()
        
    
@receiver(post_save, sender=Sales)
def update_stock(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.quantity -= instance.quantity
        product.save()
        
        
        
        
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date_purchased = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity} units"


# Create your models here.

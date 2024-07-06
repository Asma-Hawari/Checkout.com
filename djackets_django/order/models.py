from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
        ('captured', 'Captured'),
        ('refunded', 'Refunded'),
        ('voided', 'Voided'),]
        
    user  = models.ForeignKey(User, related_name='orders' , on_delete=models.CASCADE )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    paid_amount = models.DecimalField(max_digits=8 , decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100 , null = True)
    cko_token = models.CharField(max_length=100 , null = True)
    checkoutPaymentId = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"Order {self.id} - {self.status}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        # This will print the id in a string format : 123
        return '%s' % self.id






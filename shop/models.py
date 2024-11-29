from django.db import models
# This defines the  Customer and Order models with the required rship.
class Customer (models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    #when a customer is deleted, all associated orders are also deleted.
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"

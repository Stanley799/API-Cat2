from django.db import models

# This code creates customer and order models  models here.

# This Customer model stores basic information about a customer,
# including their name and email.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

def __str__(self):
    return self.name


# This Order model represents orders placed by customers.
# The ForeignKey establishes a one-to-many relationship between Customer and Order.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"


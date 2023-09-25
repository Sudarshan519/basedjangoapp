from datetime import datetime, timezone
from django.db import models

from userr.models import CustomUser

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    billing_frequency = models.IntegerField(default=1)  # Billing frequency in months
    description = models.TextField()
    # features = models.ManyToManyField('SubscriptionFeature')
    def __str__(self) -> str:
        return self.name

class SubscriptionFeature(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    



class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('canceled', 'Canceled'),
        ('pending', 'Pending'),  # Add a 'Pending' status
        ('suspended', 'Suspended'),  # Add a 'Suspended' status
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    @property
    def is_active(self):
        today = datetime.now().date()
        return self.start_date <= today <= self.end_date
    def __str__(self):
        return self.plan.name+" Plan "+self.user.email + (" Active" if self.is_active else " Expired")
class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=255)  # Store the payment method (e.g., Stripe, PayPal)

    def __str__(self):
        return f"{self.user.username} - {self.subscription.plan.name} - ${self.amount}"

django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)

    def redister(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return False

    def isExists(self):
        return Customer.objects.filter(email=self.email).exists()

    class Meta:
        verbose_name_plural="Customers"        
from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50)

    def publish(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
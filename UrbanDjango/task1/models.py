from django.db import models
from django.contrib.auth.models import User


class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyers = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

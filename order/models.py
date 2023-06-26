import datetime

from django.db import models

from .querysets import PersonQuerySet
from .managers import OrderManager


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    join_date = models.DateField(default=datetime.date.today)

    # We redefine the default manager.
    objects = PersonQuerySet.as_manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    seller = models.ForeignKey("Person", on_delete=models.CASCADE)
    sale_date = models.DateField(default=datetime.date.today)
    deleted = models.BooleanField(default=False)

    objects = OrderManager()
    historical = models.Manager()

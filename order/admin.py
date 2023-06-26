from django.contrib import admin

from .models import Order, Person

admin.site.register(Person)
admin.site.register(Order)

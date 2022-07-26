from django.contrib import admin

# Register your models here.
from cars.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
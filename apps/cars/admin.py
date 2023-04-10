from django.contrib import admin

from apps.car.models import Car, SpecialMarks, PeriodsOwnership

# Register your models here.
admin.site.register(Car)
admin.site.register(SpecialMarks)
admin.site.register(PeriodsOwnership)
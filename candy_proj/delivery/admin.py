from django.contrib import admin
from .models import Courier, CourierRegion, WorkingHour, Order, DeliveryHour

admin.site.register(Courier)
admin.site.register(CourierRegion)
admin.site.register(WorkingHour)
admin.site.register(Order)
admin.site.register(DeliveryHour)
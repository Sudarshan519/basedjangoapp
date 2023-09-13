from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Places)
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(BookingPayment)
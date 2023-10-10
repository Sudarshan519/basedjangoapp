from django.db import models

from userr.models import CustomUser
class Places(models.Model):
    address=models.CharField(max_length=256)
    image=models.ImageField(upload_to='places/')
# Create your models here.
class Hotel(models.Model):
    name=models.CharField(max_length=256)
    desc=models.CharField(max_length=256)
    address=models.CharField(max_length=256)
    price=models.FloatField()
    rating=models.FloatField()

    nearby=models.CharField(max_length=256)


# class HotelImages(models.Model):
#     image=models.ImageField(upload_to="hotels/")
#     hotel=models.ForeignKey("hotel_booking.Hotel",default=1,on_delete=models.CASCADE)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    bed_count = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} at {self.hotel}"
    

class Booking(models.Model):
    hotel_id=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room_id=models.ForeignKey(Room,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    pass

class BookingPayment(models.Model):
    amount=models.FloatField()
    booking_id=models.ForeignKey(Booking,default=1,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    pass

class PopularPlaces(models.Model):
    name=models.CharField(max_length=256)
    address=models.CharField(max_length=256)


class HotelImages(models.Model):
    image=models.ImageField(upload_to="media/popular-places")
    hotel=models.ForeignKey("hotel_booking.PopularPlaces",default=1,on_delete=models.CASCADE)

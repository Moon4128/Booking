from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='rooms', null = True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='rooms')

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return f"Room {self.number} - {self.category.title} - Capacity: {self.capacity} - Price: ${self.price}"
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f"Booking by {self.user.username} for Room {self.room.number} from {self.start_date} to {self.end_date}"
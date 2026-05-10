from django.urls import path
from core import views

urlpatterns = [
    path('', views.room_list, name = 'rooms'),
    path('booking/<int:room_id>/', views.book_room, name = 'booking'),
    path('my_bookings/', views.user_bookings, name = 'user_bookings'),
]
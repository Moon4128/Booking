from django.urls import path
from core import views

urlpatterns = [
    path('rooms/', views.room_list, name = 'room-list'),
]
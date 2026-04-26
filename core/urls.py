from django.urls import path
from core import views

urlpatterns = [
    path('', views.room_list, name = 'rooms'),
]
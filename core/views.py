from django.shortcuts import render
from .models import Room, Category, Booking

def room_list(request):
    all_rooms = Room.objects.all()
    context = {
        'rooms': all_rooms
    }
    return render (request=request, template_name='core/room_list.html', context=context)
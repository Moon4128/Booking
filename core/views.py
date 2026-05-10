from django.shortcuts import render
from .models import Room, Category, Booking
import datetime

def room_list(request):
    all_rooms = Room.objects.all()
    categories = Category.objects.all()
    
    category_id = request.GET.get('category')
    capacity = request.GET.get('capacity')
    price_max = request.GET.get('price_max')
    if category_id:
        all_rooms = all_rooms.filter(category=category_id)
    if capacity:
        all_rooms = all_rooms.filter(capacity__gte=int(capacity))
    if price_max:
        all_rooms = all_rooms.filter(price__lte=float(price_max))


    context = {
        'rooms': all_rooms,
        'categories': categories, 
        'selected_capacity': capacity,
        'selected_price_max': price_max,
        'selected_category': category_id,
    }
    return render (request=request, template_name='core/room_list.html', context=context)

def book_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    context = {
        'room': room,
    }
    if request.method == 'GET':
        return render(request=request, template_name='core/booking_form.html', context=context)
    elif request.method == 'POST':
        start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()

        user = request.user
        room = Room.objects.get(pk=room_id)

        if end_date <= start_date or start_date < str(datetime.now().date()):
            return render(request=request, template_name='core/booking_form.html', context=context)
        
        if Booking.objects.filter(room=room, start_date__lte=end_date, end_date__gte=start_date).exists():
            return render(request=request, template_name='core/booking_form.html', context=context)



        Booking.objects.create(
            user = user,
            room = room,
            start_date = start_date,
            end_date = end_date
        )

        context = {
            'bookings': Booking.objects.filter(user=user).order_by('-start_date')
        }
        return render(request=request, template_name='core/my_bookings.html', context=context)
    
def user_bookings(request):
    user = request.user
    context = {
        'bookings': Booking.objects.filter(user=user).order_by('-start_date')
    }
    return render(request=request, template_name='core/my_bookings.html', context=context)
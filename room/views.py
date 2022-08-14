from asyncio.format_helpers import extract_stack
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
# Create your views here.
@login_required
def rooms(request):
    rooms = Room.objects.filter(name=request.user.i_am)
    #added this for retriving other groups also -dinesh
    other_rooms = Room.objects.filter(enroll_aluminis = request.user)
    #upto this -dinesh
    return render(request, 'room/rooms.html', {'rooms': rooms,'other_rooms':other_rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    return render(request, 'room/room.html', {'room': room, 'messages':messages})




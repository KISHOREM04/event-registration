

from django.shortcuts import render, redirect
from .models import Event, Registration

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def registration(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        registration = Registration(event=event, name=name, email=email, phone=phone)
        registration.save()
        return redirect('event_list')
    return render(request, 'registration.html', {'event': event})
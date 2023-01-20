from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        contact = Contact(name = name, email = email, subject = subject, message = message)
        contact.save()
        messages.success(request, 'Message Sent! The Advaita Mail Man Is On the Way :)')

    return render(request, 'contact.html')

def eventdetails(request, slug):
    if slug == "technicalevents":
        heading = "Technical Events"
        headerimg = '/static/images/events/tech.png'
    elif slug == "culturalevents":
        heading = "Cultural Events"
        headerimg = '/static/images/events/tech.png'
    events = Event.objects.filter(slug = slug)
    context = {'events':events, 'heading':heading, 'headerimg':headerimg}
    return render(request, 'eventdetails.html', context)


def pronites(request):
    return render(request, 'pronites.html')

def sponsors(request):
    return render(request, 'sponsors.html')
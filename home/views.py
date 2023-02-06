from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Contact
from django.contrib import messages


def custom_404(request, exception):
    return render(request,'404.html')

def custom_500(request):
    return render(request,'404.html')

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
    elif slug == "filmandtheatre":
        heading = "Film and Theatre Litfest"
        headerimg = '/static/images/events/tech.png'
    elif slug == "paracosm":
        heading = "Paracosm"
        headerimg = '/static/images/events/tech.png'
    elif slug == "esports":
        heading = "E-Sports"
        headerimg = '/static/images/events/tech.png'
    elif slug == "food":
        heading = "Food"
        headerimg = '/static/images/events/tech.png'
    elif slug == "csr":
        heading = "CSR"
        headerimg = '/static/images/events/tech.png'
    events = Event.objects.filter(slug = slug).order_by('-timeslot')
    context = {'events':events, 'heading':heading, 'headerimg':headerimg}
    return render(request, 'eventdetails.html', context)


def pronites(request):
    pronites = Event.objects.filter(slug = "pronites").order_by('-timeslot')
    context = {'pronites': pronites}
    return render(request, 'pronites.html', context)

def sponsors(request):
    return render(request, 'sponsors.html')
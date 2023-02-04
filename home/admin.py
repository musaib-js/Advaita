from django.contrib import admin
from .models import Event, Contact, Sponsorship

admin.site.register((Event, Contact, Sponsorship))

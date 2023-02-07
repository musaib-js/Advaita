from django.contrib import admin
from .models import Event, Contact, Sponsorship, Sponsor

admin.site.register((Event, Contact, Sponsorship, Sponsor))

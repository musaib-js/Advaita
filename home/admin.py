from django.contrib import admin
from .models import Event, Contact

admin.site.register((Event, Contact))

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('events/', views.events, name = "events"),
    path('contact/', views.contact, name = "contact"),
    path('pronites/', views.pronites, name = "pronites"),
    path('sponsors/', views.sponsors, name = "sponsors"),
    path('events/<str:slug>/', views.eventdetails, name = "eventdetails"),
]

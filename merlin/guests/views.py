from django.shortcuts import render
from merlin.guests.models import Guest
from django.views.generic.list import ListView

# Create your views here.
class GuestListView(ListView):
    model = Guest


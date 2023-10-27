from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

class ItemList(ListView):
    model = Item
# Create your views here.

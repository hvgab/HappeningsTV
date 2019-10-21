from django.shortcuts import render
from . import models

def home(request):
    return render(request, 'app/home.html')

def tv(request, tag):
    tag = models.Tag.objects.get(name=tag)
    happenings = models.Happening.objects.all()
    return render(request, 'app/tv.html', {'happenings':happenings})

def register_to_event(request):
    """Form to register to event.
    Write in name ++ and select event.

    """
    pass
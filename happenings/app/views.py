from django.shortcuts import render
from . import models


def tv(request):
    happening = models.Happening.objects.first()
    return render(request, 'app/tv.html', {'happening':happening})

def register_to_event(request):
    """Form to register to event.
    Write in name ++ and select event.

    """
    pass
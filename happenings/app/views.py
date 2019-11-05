from django.shortcuts import render
from . import models

def home(request):
    tags = models.Tag.objects.all()
    active_happenings = models.Happening.happenings.active().order_by('start_date', 'end_date')
    upcoming_happenings = models.Happening.happenings.upcoming().order_by('start_date', 'end_date')
    finished_happenings = models.Happening.happenings.finished().order_by('-end_date', 'start_date')
    return render(request, 'app/home.html', dict(tags=tags, active_happenings=active_happenings, upcoming_happenings=upcoming_happenings, finished_happenings=finished_happenings))

def tv(request, tag_name):
    tag = models.Tag.objects.get(name__iexact=tag_name)
    happenings = models.Happening.happenings.active().filter(tags__in=[tag]).all()
    return render(request, 'app/tv.html', dict(happenings=happenings))

def register_to_event(request):
    """Form to register to event.
    Write in name ++ and select event.

    """
    pass
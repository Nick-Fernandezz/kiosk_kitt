from django.shortcuts import render
from .models import *

# Create your views here.

def index_timetable_page(request):
    timetable_bots = TimetableBot.objects.filter(is_active=True)
    return render(request, 'timetable/index.html', context={
        'timetable_bots': timetable_bots
    })

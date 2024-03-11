from django.shortcuts import render

# Create your views here.

def index_timetable_page(request):
    return render(request, 'timetable/index.html')

from django.shortcuts import render
from .models import *


def index_page(request):

    index_slides = Slider.objects.filter(is_active=True)
    
    
    return render(request, 'main/index_page.html', context={
        'index_slides': index_slides,
    })
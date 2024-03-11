from django.shortcuts import render
from .models import *


# Create your views here.
def index_social_media_page(request):
    social_medias = SocialMedia.objects.filter(is_active=True)

    return render(request, 'social_media/index.html', context={
        'social_medias': social_medias
    })
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_social_media_page, name='index_social_media_page')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

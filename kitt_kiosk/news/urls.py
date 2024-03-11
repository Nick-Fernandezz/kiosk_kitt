from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_news_page, name="index_news_page"),
    path('<int:news_id>/', detail_news_page, name='detail_news_page'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


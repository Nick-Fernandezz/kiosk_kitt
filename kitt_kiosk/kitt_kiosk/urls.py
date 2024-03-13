"""
URL configuration for kitt_kiosk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from main import urls as main_urls
from social_media import urls as sc_urls
from timetable import urls as timetable_urls
from news import urls as news_urls
from additional_edu import urls as add_edu_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls)),
    path('social_media/', include(sc_urls)),
    path('timetable/', include(timetable_urls)),
    path('news/', include(news_urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('additional/', include(add_edu_urls))
]
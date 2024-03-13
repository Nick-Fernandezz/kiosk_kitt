from django.urls import path
from .views import *


urlpatterns = [
    path('', index_additional_education_page, name="index_additional_education_page"),
    path('<int:doc_id>', detail_doc_page, name='detail_doc_page')

]


from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import *
# Create your views here.

def index_additional_education_page(request):
    docs = Docs.objects.all().order_by('-created_date')
    return render(request, 'additional_edu/index.html', context={
        'docs': docs,
    })


def detail_doc_page(request, doc_id):
    docs = get_list_or_404(DocsScan, doc__id=doc_id)
    print(docs)
    return render(request, 'additional_edu/details_doc.html', context={
        'docs': docs
    })

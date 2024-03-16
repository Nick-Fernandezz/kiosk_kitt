from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .models import NewsImages, News
# Create your views here.

def index_news_page(request):

    news = News.objects.filter(is_active=True).order_by('-created_date')
    res_news = []
    for new in news:
        res_news.append(NewsImages.objects.filter(news=new)[0])

    # news_list = NewsImages.objects.filter(news__is_active=True).distinct('news').order_by('-news__created_date')
    paginator = Paginator(res_news, 25)
    res_news = paginator.get_page(request.GET.get('page', 1))
    
    return render(request, 'news/index.html', context={
        'news': res_news
    })


def detail_news_page(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news_images = NewsImages.objects.filter(news__id=news_id)

    return render(request, 'news/detail_news_page.html', context={
        'news': news,
        'news_images': news_images
    })


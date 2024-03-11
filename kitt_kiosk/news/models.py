from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class News(models.Model):

    title = models.CharField('Заголовок', max_length=200)
    text = RichTextField('Текст')
    is_active = models.BooleanField('Активно', default=True)
    created_date = models.DateTimeField('Дата написания', auto_now_add=True)
    
    class Meta:
        verbose_name="новость"
        verbose_name_plural = "Новости"

    def __str__(self) -> str:
        return self.title

class NewsImages(models.Model):

    news = models.ForeignKey(News, models.CASCADE, related_name='news')
    image = models.ImageField('Фото', upload_to=f'news/images/%Y/%m/%d/%H-%M-%S/')

    class Meta:
        verbose_name="фото"
        verbose_name_plural = "Фотографии"

    def __str__(self) -> str:
        return str(self.id)

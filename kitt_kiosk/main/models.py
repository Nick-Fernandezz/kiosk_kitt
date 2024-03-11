from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Slider(models.Model):

    title = models.CharField(max_length=200, verbose_name="Заголовок", null=True, blank=True)
    link = models.URLField(verbose_name="Ссылка", null=True, blank=True)
    media = models.ImageField(verbose_name="Фото", upload_to="main/slider/%Y-%m-%d-%H-%M-%S/")
    owner = models.ForeignKey(User, models.CASCADE, verbose_name="Создатель поста", auto_created=True, default=1)
    is_active = models.BooleanField(verbose_name='Отображать', default=True)
    created_date = models.DateTimeField(verbose_name='Время создания', auto_now_add=True, editable=False)

    class Meta:
        verbose_name="рекламный слайд"
        verbose_name_plural = "Рекламные слайды"

    def __str__(self) -> str:
        return f'{self.id} {self.title}'


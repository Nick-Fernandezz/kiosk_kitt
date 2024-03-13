from django.db import models

from django_currentuser.db.models import CurrentUserField
# Create your models here.

class Slider(models.Model):

    title = models.CharField(max_length=200, verbose_name="Заголовок", null=True, blank=True)
    is_active_title = models.BooleanField(verbose_name='Отображать заголовок', default=False)
    # link = models.URLField(verbose_name="Ссылка", null=True, blank=True)
    media = models.ImageField(verbose_name="Фото", upload_to="main/slider/%Y-%m-%d-%H-%M-%S/")
    updated_date = models.DateTimeField('Дата последнего изменения', auto_now=True)
    created_by = CurrentUserField(verbose_name="Создал", on_delete=models.CASCADE, default=1, related_name='slider_created_by')
    updated_by = CurrentUserField(verbose_name="Изменил", on_update=True, related_name='slider_updated_by')
    is_active = models.BooleanField(verbose_name='Отображать', default=True)
    created_date = models.DateTimeField(verbose_name='Время создания', auto_now_add=True, editable=False)

    class Meta:
        verbose_name="рекламный слайд"
        verbose_name_plural = "Рекламные слайды"


    def __str__(self) -> str:
        return f'{self.id} {self.title}'


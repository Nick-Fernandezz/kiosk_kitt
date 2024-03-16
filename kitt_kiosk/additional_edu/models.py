from django.db import models
from django_currentuser.db.models import CurrentUserField

class Docs(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    created_date = models.DateField('Дата создания', auto_now_add=True)
    # updated_date = models.DateField('Дата последнего изменения', auto_now=True)
    updated_date = models.DateField('Дата последнего изменения', auto_now=True, auto_now_add=False)
    created_by = CurrentUserField(verbose_name="Создал", on_delete=models.CASCADE, related_name="docs_created_by")
    updated_by = CurrentUserField(verbose_name="Последнее изменение", on_update=True, related_name="docs_updated_by")

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "Документы"

class DocsScan(models.Model):
    doc = models.ForeignKey(Docs, on_delete=models.CASCADE)
    image = models.ImageField('Скан документа', upload_to='additional_edu/scans/%Y/%m/%d/%H-%M-%S/')

    class Meta:
        verbose_name = "скан"
        verbose_name_plural = "Сканы"





from django.db import models
from django_currentuser.db.models import CurrentUserField
# Create your models here.
# class AdditionalEducation(models.Model):
#     title = models.CharField('Название')



# class TimetableAdditionalEducation(models.Model):
#     days = (
#         ('Понедельник', 1),
#         ('Вторник', 2),
#         ('Среда', 3),
#         ('Четверг', 4),
#         ('Пятница', 5),
#         ('Суббота', 6)
#     )
#     add_edu = models.ForeignKey(AdditionalEducation, on_delete=models.CASCADE, verbose_name='Кружок')
#     day = models.CharField("День недели", choices=days)

class Docs(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_date = models.DateTimeField('Дата последнего изменения', auto_now=True)
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





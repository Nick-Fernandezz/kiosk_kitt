from django.db import models
from django_currentuser.db.models import CurrentUserField
# Create your models here.



class TimetableBot(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    bg_img = models.ImageField('Изображение', upload_to='social_media/titles/%Y/%m/%d-%H-%M-%S/')
    qr_code = models.ImageField('QR Код', upload_to='social_media/qrcodes/%Y/%m/%d-%H-%M-%S/') 
    is_active = models.BooleanField('Активно', default=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_date = models.DateTimeField('Дата изменения', auto_now=True)
    created_by = CurrentUserField(verbose_name="Создал", on_delete=models.CASCADE, default=1, related_name='TimetableBot_created_by')
    updated_by = updated_by = CurrentUserField(verbose_name="Изменил", on_update=True, related_name='TimetableBot_updated_by')

    class Meta:
        verbose_name='бот расписания'
        verbose_name_plural="Боты расписания"
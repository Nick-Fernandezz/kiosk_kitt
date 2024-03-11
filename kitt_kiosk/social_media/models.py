from django.db import models

# Create your models here.


class SocialMedia(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    bg_img = models.ImageField('Изображение', upload_to='social_media/titles/%Y/%m/%d-%H-%M-%S/')
    qr_code = models.ImageField('QR Код', upload_to='social_media/qrcodes/%Y/%m/%d-%H-%M-%S/') 
    is_active = models.BooleanField('Активно', default=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name='социальная сеть'
        verbose_name_plural="Социальные сети"
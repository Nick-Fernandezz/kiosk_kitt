from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основное', {
            'fields': (
                'title',
                'is_active'
            )
        }),
        ('Изображения', {
            'fields': (
                'bg_img',
                'qr_code'
            )
        }),
        (None, {
            'fields': (
                'created_date',
            )
        })
    )
    readonly_fields = ('created_date', )
    list_display = ('id', 'is_active', 'title', 'created_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_active', )

from django.contrib import admin
from .models import *

from django.utils.safestring import mark_safe
# Register your models here.

admin.site.site_header = "Администрирование киосков ГАПОУ КК КИТТ"


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'is_active_title'),
                'is_active',
            )
        }),
        ('Медиа', {
            'fields': (
                'media',
                'media_image'
                
            )
        }),
        ('Дополнительная информация', {
            'fields': (
                'created_date',
                'updated_date',
                'created_by',
                'updated_by'

            )
        })
    )
    readonly_fields = ('created_by', 'updated_by', 'created_date', 'updated_date', 'media_image')
    list_display = ('id' ,'is_active', 'title', 'created_by', 'created_date', 'media_image')
    list_display_links = ('id' ,'title', 'created_by')
    list_editable = ('is_active',)

    def media_image(self, obj):
        return mark_safe(f'<img src="{obj.media.url}" width="100px">')
    
    media_image.short_description = "Превью"

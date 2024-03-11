from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "Администрирование киосков ГАПОУ КК КИТТ"


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'is_active',
                'owner'
            )
        }),
        ('Медиа', {
            'fields': (
                'media',
                'link'
            )
        }),
        ('Дополнительная информацию', {
            'fields': (
                'created_date',
            )
        })
    )
    readonly_fields = ('owner', 'created_date')
    list_display = ('id' ,'is_active', 'title', 'owner', 'created_date')
    list_display_links = ('id' ,'title', 'owner')
    list_editable = ('is_active',)


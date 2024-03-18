from django.contrib import admin
from .models import TimetableBot
# Register your models here.

@admin.register(TimetableBot)
class AdminTimetableBot(admin.ModelAdmin):
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
        ("Дополнительно", {
            "classes": ["collapse"],
            'fields': (
                'created_date',
                'updated_date',
                'created_by',
                'updated_by'
            )
        })
    )
    readonly_fields = ('created_date', 'updated_date', 'created_by', 'updated_by')
    list_display = ('id', 'is_active', 'title', 'created_date', 'created_by',)
    list_display_links = ('id', 'title')
    list_editable = ('is_active', )

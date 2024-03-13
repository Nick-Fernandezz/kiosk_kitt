from django.contrib import admin
from .models import *
# Register your models here.

class AdminDocsScan(admin.StackedInline):
    model = DocsScan
    max_num = 10
    extra = 0

@admin.register(Docs)
class AdminDocs(admin.ModelAdmin):
    
    inlines = [AdminDocsScan,]

    fieldsets = (
        (
            None, {
                'fields': ('title',)
            }
        ),
        (
            'Дополнительная информация', {
                "classes": ["collapse"],
                "fields": (
                    'created_date',
                    'updated_date',
                    'created_by',
                    'updated_by'
                )
            }
        )
    )

    list_display = ('title', 'created_date', 'created_by')
    list_display_links = ('title', 'created_date', 'created_by')
    readonly_fields = ('created_date', 'updated_date', 'created_by', 'updated_by')

    

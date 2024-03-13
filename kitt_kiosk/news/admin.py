from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import *


# Register your models here.

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'

class AdminNewsImagesInline(admin.StackedInline):
    model = NewsImages
    max_num = 10
    extra = 0

@admin.register(News)
class AdminNewsImages(admin.ModelAdmin):
    inlines = [AdminNewsImagesInline,]
    list_display = ('id', 'is_active', 'title', 'created_date')
    readonly_fields = ('created_by', 'updated_by')
    list_display_links = ('id', 'title', 'created_date')
    list_editable = ('is_active', )


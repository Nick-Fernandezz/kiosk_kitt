# Generated by Django 5.0.2 on 2024-03-13 07:46

import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_slider_usercreated'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='usercreated',
        ),
        migrations.AddField(
            model_name='slider',
            name='created_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slider_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Создал'),
        ),
        migrations.AddField(
            model_name='slider',
            name='is_active_title',
            field=models.BooleanField(default=False, verbose_name='Отображать заголовок'),
        ),
        migrations.AddField(
            model_name='slider',
            name='updated_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='slider_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Изменил'),
        ),
        migrations.AddField(
            model_name='slider',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
    ]

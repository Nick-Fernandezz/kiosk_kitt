# Generated by Django 5.0.3 on 2024-03-16 11:49

import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='timetablebot',
            name='created_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TimetableBot_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Создал'),
        ),
        migrations.AddField(
            model_name='timetablebot',
            name='updated_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='TimetableBot_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Изменил'),
        ),
        migrations.AddField(
            model_name='timetablebot',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]

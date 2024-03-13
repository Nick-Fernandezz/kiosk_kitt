# Generated by Django 5.0.2 on 2024-03-13 09:14

import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional_edu', '0002_docs_created_by_docs_updated_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='updated_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='docs_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Последнее изменение'),
        ),
        migrations.AlterField(
            model_name='docs',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
    ]

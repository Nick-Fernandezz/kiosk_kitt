# Generated by Django 5.0.2 on 2024-03-13 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional_edu', '0003_docs_updated_by_alter_docs_updated_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docs',
            options={'verbose_name': 'документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterModelOptions(
            name='docsscan',
            options={'verbose_name': 'скан', 'verbose_name_plural': 'Сканы'},
        ),
        migrations.AlterField(
            model_name='docsscan',
            name='image',
            field=models.ImageField(upload_to='additional_edu/scans/%Y/%m/%d/%H-%M-%S/', verbose_name='Скан документа'),
        ),
    ]

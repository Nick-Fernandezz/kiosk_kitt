# Generated by Django 5.0.2 on 2024-03-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_slider_media_alter_slider_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('WhatsApp', 'WhatsApp'), ('VK', 'VK'), ('Telegram', 'Telegram'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('OK', 'OK'), ('TikTok', 'TikTok'), ('Twitter', 'Twitter'), ('YouTube', 'YouTube')], default=('WhatsApp', 'WhatsApp'), max_length=50)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'соц. сеть',
                'verbose_name_plural': 'Соц. сети',
            },
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-31 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingsettings',
            options={'ordering': ['-id'], 'verbose_name': 'Настройка рассылки', 'verbose_name_plural': 'Настройки рассылки'},
        ),
    ]
# Generated by Django 4.0 on 2021-12-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todosaz_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال است/نیست'),
        ),
    ]

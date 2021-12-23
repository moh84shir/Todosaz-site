# Generated by Django 4.0 on 2021-12-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('subject', models.CharField(max_length=120, verbose_name='موضوع')),
                ('short_desc', models.CharField(max_length=200, verbose_name='توضیحات کوتاه')),
                ('text', models.TextField(verbose_name='متن')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='روز انتشار')),
            ],
            options={
                'verbose_name': 'خبر',
                'verbose_name_plural': 'اخبار',
            },
        ),
    ]

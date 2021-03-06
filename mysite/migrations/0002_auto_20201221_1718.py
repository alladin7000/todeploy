# Generated by Django 3.1.4 on 2020-12-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, verbose_name='number of views'),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-22 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20201221_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='news', to='mysite.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

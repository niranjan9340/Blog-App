# Generated by Django 5.0.3 on 2024-04-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-08 12:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_post_bookmarks'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]

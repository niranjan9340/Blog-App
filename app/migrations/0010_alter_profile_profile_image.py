# Generated by Django 5.0.3 on 2024-04-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

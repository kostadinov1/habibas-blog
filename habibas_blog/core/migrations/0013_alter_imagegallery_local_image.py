# Generated by Django 4.0.4 on 2022-05-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_imagegallery_url_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallery',
            name='local_image',
            field=models.ImageField(blank=True, null=True, upload_to='mediafiles/images'),
        ),
    ]

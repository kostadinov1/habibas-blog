# Generated by Django 4.0.4 on 2022-05-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_gender_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default='2020-12-12'),
            preserve_default=False,
        ),
    ]

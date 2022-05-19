# Generated by Django 4.0.4 on 2022-05-19 10:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import habibas_blog.common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('has_profile', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=30, validators=[habibas_blog.common.validators.validate_only_letters, django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=30, validators=[habibas_blog.common.validators.validate_only_letters, django.core.validators.MinLengthValidator(2)])),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('LGBT+', 'LGBT+'), ('Prefer Not to Tell', 'Prefer Not to Tell')], max_length=30)),
                ('phone', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('image_local', models.ImageField(blank=True, null=True, upload_to='profile_images', validators=[habibas_blog.common.validators.MaxFileSizeInMbImageValidator(5)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

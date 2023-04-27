# Generated by Django 4.2 on 2023-04-27 19:44

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_userprofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar-default.svg', null=True, upload_to=users.models.uploaded_avatars_directory_path),
        ),
    ]

# Generated by Django 4.2 on 2023-04-23 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='temp', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

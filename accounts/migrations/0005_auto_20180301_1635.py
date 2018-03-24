# Generated by Django 2.0.2 on 2018-03-01 07:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180301_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=0, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed.", regex='^[0-9]+$')], verbose_name='phone number'),
            preserve_default=False,
        ),
    ]
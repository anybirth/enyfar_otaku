# Generated by Django 2.0.4 on 2018-04-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemimage',
            name='image_path',
        ),
        migrations.AddField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(upload_to='main/img/item/', verbose_name='画像'),
        ),
    ]
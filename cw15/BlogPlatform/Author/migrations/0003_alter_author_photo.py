# Generated by Django 4.2.3 on 2023-07-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0002_author_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(default='media/images/unknown.png', upload_to='images/'),
        ),
    ]

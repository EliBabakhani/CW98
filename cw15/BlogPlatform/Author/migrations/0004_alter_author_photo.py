# Generated by Django 4.2.3 on 2023-07-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0003_alter_author_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(default='images/unknown.png', upload_to='images/'),
        ),
    ]

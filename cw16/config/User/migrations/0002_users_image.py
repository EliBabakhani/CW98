# Generated by Django 4.2.3 on 2023-07-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(default='images/unknown.png', upload_to='images'),
        ),
    ]

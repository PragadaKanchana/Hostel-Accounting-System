# Generated by Django 5.0 on 2024-01-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Has', '0011_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='vacancy',
            field=models.IntegerField(default='0'),
        ),
    ]

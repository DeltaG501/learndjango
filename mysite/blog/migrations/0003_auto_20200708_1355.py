# Generated by Django 3.0.8 on 2020-07-08 05:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200707_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 5, 55, 1, 817502, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-16 14:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191015_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='happening',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='happening',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 16, 14, 32, 39, 41670, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

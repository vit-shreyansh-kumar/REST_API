# Generated by Django 2.2.3 on 2019-08-25 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='finish_time',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='start_time',
        ),
        migrations.AddField(
            model_name='pizza',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 25, 16, 53, 29, 407598)),
        ),
    ]

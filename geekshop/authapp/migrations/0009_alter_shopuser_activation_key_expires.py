# Generated by Django 3.2.11 on 2022-01-17 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20220117_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 19, 15, 2, 47, 132743, tzinfo=utc), verbose_name='Истечение срока активации'),
        ),
    ]
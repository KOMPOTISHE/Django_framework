# Generated by Django 4.0 on 2022-01-18 08:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20220118_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 8, 53, 25, 524008, tzinfo=utc), verbose_name='Истечение срока активации'),
        ),
    ]
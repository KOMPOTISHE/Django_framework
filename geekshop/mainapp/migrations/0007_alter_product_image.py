# Generated by Django 4.0 on 2021-12-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='products_images/default.jpg', upload_to='products_images'),
        ),
    ]

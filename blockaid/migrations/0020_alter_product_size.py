# Generated by Django 4.2 on 2023-07-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockaid', '0019_product_quantity_product_size_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_product_is_discount_alter_category_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_discount',
            field=models.CharField(choices=[('Discount', 'discount'), ('Nodiscount', 'nodiscount')], default='Nodiscount', max_length=10),
        ),
    ]

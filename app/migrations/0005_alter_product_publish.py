# Generated by Django 5.0.4 on 2024-04-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product_is_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publish',
            field=models.CharField(choices=[('Publish', 'publish'), ('Nopublish', 'nopublish')], default='Publish', max_length=9),
        ),
    ]

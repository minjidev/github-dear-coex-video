# Generated by Django 3.1.13 on 2021-09-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='product_interest_count',
            new_name='product_like_count',
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_reserve_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
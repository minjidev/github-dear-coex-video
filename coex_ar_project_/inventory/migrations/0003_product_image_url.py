# Generated by Django 3.1.13 on 2021-09-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_useraction'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default='none', max_length=150),
            preserve_default=False,
        ),
    ]

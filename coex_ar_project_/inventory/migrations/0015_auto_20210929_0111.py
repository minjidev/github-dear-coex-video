# Generated by Django 3.1.13 on 2021-09-29 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20210929_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraction',
            name='date_time',
            field=models.DateTimeField(default='2021-09-29 01:11:41'),
        ),
    ]

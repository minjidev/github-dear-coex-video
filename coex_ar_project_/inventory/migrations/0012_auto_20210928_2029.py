# Generated by Django 3.1.13 on 2021-09-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20210928_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraction',
            name='date_time',
            field=models.DateTimeField(default='2021-09-28 20:29:46'),
        ),
    ]
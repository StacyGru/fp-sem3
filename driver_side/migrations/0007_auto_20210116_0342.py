# Generated by Django 3.1.5 on 2021-01-15 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_side', '0006_auto_20210116_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='number',
            field=models.CharField(max_length=15),
        ),
    ]

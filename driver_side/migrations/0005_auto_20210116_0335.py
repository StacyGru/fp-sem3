# Generated by Django 3.1.5 on 2021-01-15 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver_side', '0004_auto_20210116_0331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='model_id',
            new_name='model_details',
        ),
    ]
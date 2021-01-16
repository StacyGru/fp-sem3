# Generated by Django 3.1.5 on 2021-01-15 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver_side', '0002_auto_20210116_0228'),
        ('client_side', '0005_auto_20210116_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='from_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_place', to='driver_side.street'),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_place', to='driver_side.street'),
        ),
    ]
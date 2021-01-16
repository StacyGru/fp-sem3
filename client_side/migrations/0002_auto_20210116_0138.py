# Generated by Django 3.1.5 on 2021-01-15 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver_side', '0001_initial'),
        ('client_side', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discountcard',
            old_name='client',
            new_name='client_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='client',
            new_name='client_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='gender',
            new_name='driver_gender',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='operator',
            new_name='operator_id',
        ),
        migrations.AddField(
            model_name='ride',
            name='car_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='driver_side.car'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ride',
            name='driver_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='driver_side.driver'),
            preserve_default=False,
        ),
    ]
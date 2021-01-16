# Generated by Django 3.1.5 on 2021-01-15 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver_side', '0003_auto_20210116_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gearbox', models.CharField(choices=[('автомат', 'автомат'), ('механика', 'механика')], max_length=15)),
                ('seats', models.PositiveSmallIntegerField()),
                ('engine', models.PositiveSmallIntegerField()),
                ('wheel_side', models.CharField(choices=[('слева', 'слева'), ('справа', 'справа')], max_length=15)),
                ('child_seat', models.CharField(choices=[('есть', 'есть'), ('нет', 'нет')], max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='model_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver_side.cardetails'),
        ),
        migrations.DeleteModel(
            name='CarModel',
        ),
    ]

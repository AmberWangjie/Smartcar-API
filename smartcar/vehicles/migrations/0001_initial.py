# Generated by Django 2.0 on 2017-12-23 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('START', 'start'), ('STOP', 'stop')], max_length=100)),
                ('status', models.CharField(choices=[('success', 'executed'), ('error', 'failed')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('locked', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('vin', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('doorCount', models.IntegerField(choices=[(2, 'twoDoorCoupe'), (4, 'fourDoorSedan')])),
                ('driveTrain', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='security',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doors', to='vehicles.Vehicle'),
        ),
        migrations.AddField(
            model_name='fuel',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuelLevel', to='vehicles.Vehicle'),
        ),
        migrations.AddField(
            model_name='engine',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engineStatus', to='vehicles.Vehicle'),
        ),
        migrations.AddField(
            model_name='battery',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batteryLevel', to='vehicles.Vehicle'),
        ),
    ]

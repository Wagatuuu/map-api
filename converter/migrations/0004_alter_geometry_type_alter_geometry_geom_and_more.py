# Generated by Django 4.1 on 2022-09-06 12:40

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0003_alter_properties_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geometry',
            name='Type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='geometry',
            name='geom',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.gis.db.models.fields.PointField(srid=4326), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='geometry',
            name='place',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='noiselevel',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='place',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='pleasantness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='properties',
            name='time_ISO8601',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='time_epoch',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='timelength',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='track_uuid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

from django.contrib.gis.db import models as gis_models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Geometry(gis_models.Model):
    place = gis_models.CharField(max_length=200, blank=True)
    Type = gis_models.CharField(max_length=20)
    geom = ArrayField(base_field=gis_models.PointField())

    class Meta:
        verbose_name_plural = 'Geometry'
    
    def __str__(self):
        return self.place

class Properties(gis_models.Model):
    place = gis_models.ForeignKey(Geometry, on_delete=gis_models.CASCADE)
    pk_track = gis_models.IntegerField(primary_key=True, blank=True)
    noiselevel = gis_models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    timelength = gis_models.DecimalField(max_digits=20, decimal_places=1, blank=True)
    tags = ArrayField(base_field=gis_models.CharField(max_length=20), blank=True)
    time_epoch = gis_models.IntegerField(blank=True)
    pleasantness = gis_models.IntegerField(blank=True)
    track_uuid = gis_models.CharField(max_length=1000, blank=True)
    time_ISO8601 = gis_models.DateTimeField(blank=True)

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.place.place
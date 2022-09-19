from django.contrib.gis.db import models as gis_models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Geometry(gis_models.Model):
    place = gis_models.CharField(max_length=200, blank=True, null=True)
    Type = gis_models.CharField(max_length=20, null=True)
    geom = ArrayField(base_field=gis_models.PointField(), blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Geometry'
    
    def __str__(self):
        return self.place

class Properties(gis_models.Model):
    place = gis_models.CharField(max_length=200, blank=True, null=True)
    pk_track = gis_models.IntegerField(primary_key=True, blank=True)
    noiselevel = gis_models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    timelength = gis_models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    tags = ArrayField(base_field=gis_models.CharField(max_length=20), blank=True, null=True)
    time_epoch = gis_models.CharField(max_length=200, blank=True, null=True)
    pleasantness = gis_models.IntegerField(blank=True, null=True)
    track_uuid = gis_models.CharField(max_length=1000, blank=True, null=True)
    time_ISO8601 = gis_models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.place

class UserProfile(AbstractUser):
    username = gis_models.CharField(max_length=120, unique=True)
    email = gis_models.EmailField(max_length=100)
    password = gis_models.CharField(('password'), max_length=128, help_text=("use'[algo]$[salt]$[hexdigest]'"))
    created_on = gis_models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.username
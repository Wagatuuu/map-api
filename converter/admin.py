from django.contrib import admin
from .models import Properties, Geometry, UserProfile, UserUploadedData
# Register your models here.
admin.site.register(Properties)
admin.site.register(Geometry)
admin.site.register(UserProfile)
admin.site.register(UserUploadedData)
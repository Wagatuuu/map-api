from tokenize import Pointfloat
from rest_framework import serializers
from converter.models import Properties

class NoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ('__all__')
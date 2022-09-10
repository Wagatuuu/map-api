from rest_framework.response import Response
from converter.serializers import NoiseSerializer
from converter.models import Properties
from rest_framework import generics, permissions

# Create your views here.
class NoiseInfoView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'pk'
    serializer_class = NoiseSerializer

    def get_queryset(self):
        return Properties.objects.all()
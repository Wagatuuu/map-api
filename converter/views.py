from rest_framework.response import Response
from converter.serializers import NoiseSerializer, ProfileSerializer, UserUploadSerializer
from converter.models import Properties
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class NoiseInfoView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'pk'
    serializer_class = NoiseSerializer

    def get_queryset(self):
        return Properties.objects.all()

@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def register(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'success'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            serializer = UserUploadSerializer(data=request.data)    
            data = {}                       

            if serializer.is_valid():
                userdata = serializer.save()
                userdata.user = request.user
                userdata.save()
                data['response'] = 'success'
                data['place'] = userdata.place
                data['noiselevel'] = userdata.noiselevel
                data['timelength'] = userdata.timelength
                data['noise_type'] = userdata.noise_type
                data['pleasantness'] = userdata.pleasantness
            else:
                data = serializer.errors
            return Response(data)
    return Response({'failed': 'user not authenticated'})

@permission_classes((permissions.AllowAny,))
class TokenView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)
        serializer = ProfileSerializer(user)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({"token": user.auth_token.key, "user": serializer.data})
        else:
            return Response({"error": "Wrong credentials"}, status = status.HTTP_400_BAD_REQUEST)

class CurView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    
    def get(self, request):
        res = []
        serializer = ProfileSerializer(request.user)
        res.append(serializer.data)
        return Response(res)
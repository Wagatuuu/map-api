from dataclasses import field
from rest_framework import serializers
from converter.models import Properties, UserProfile, UserUploadedData

class UserUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUploadedData
        field = ('user', 'place', 'noiselevel', 'timelength', 'noise_type', 'pleasantness')

        def save(self):
            data = UserUploadedData(
                place = self.validated_data['place'],
                noiselevel = self.validated_data['noiselevel'],
                timelength = self.validated_data['timelength'],
                noise_type = self.validated_data['noise_type'],
                pleasantness = self.validated_data['pleasantness'],
            )
            data.user = self.request.user
            data.save()
            return data

class NoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = UserProfile(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'passwords do not match'})
        user.set_password(password)
        user.save()
        return user
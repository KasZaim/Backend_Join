#api/serializer.py
from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs= {
            'password':{
                'write_only': True
            }
        }
        
    def save(self):
        email = self.validated_data['email']
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        
        if User.objects.filter(email=email).exists():
           raise serializers.ValidationError({'email': 'A user with this email already exists.'})
        
        if pw != repeated_pw:
            raise serializers.ValidationError({'error':'passwords dont match'})
        
        account = User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(pw)
        account.save()
        return account
#api/serializer.py
from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User
from ..models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields =['initials', 'color']
        
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile', read_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'profile']

        
        
class RegistrationSerializer(serializers.ModelSerializer):
    # repeated_password = serializers.CharField(write_only=True)
    profile = UserProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password',  'profile'] #'repeated_password'
        extra_kwargs= {
            'password':{
                'write_only': True
            }
        }
        
    def save(self):
        email = self.validated_data['email']
        pw = self.validated_data['password']
        # repeated_pw = self.validated_data['repeated_password']
        profile_data = self.validated_data.pop('profile')
        
        if User.objects.filter(email=email).exists():
           raise serializers.ValidationError({'email': 'A user with this email already exists.'})
        
        # if pw != repeated_pw:
        #     raise serializers.ValidationError({'error':'passwords dont match'})
        
        account = User(email=email,username=self.validated_data['username'])
        account.set_password(pw)
        account.save()
        UserProfile.objects.create(user=account, **profile_data)
        return account
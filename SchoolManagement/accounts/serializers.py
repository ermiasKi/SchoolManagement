from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'created_at', 'updated_at', 'profile_picture']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'profile_picture', 'first_name', 'last_name', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data['role'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']


    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])

        if user and user.is_authenticated:
            return user
        return serializers.ValidationError("username or password is incorrect")
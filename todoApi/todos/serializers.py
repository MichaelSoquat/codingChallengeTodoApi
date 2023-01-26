from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth import password_validation
from rest_framework.validators import UniqueValidator

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'state', 'priority', 'creation_date', 'creator']
        
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username",]

class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField(min_length = 4, max_length = 20, validators = [UniqueValidator(queryset = User.objects.all())])
    password = serializers.CharField(min_length = 8, max_length = 64)
    password_confirmation = serializers.CharField(min_length = 8, max_length = 64)

    def validate(self, attrs):

        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError("Passwords didn't match.")

        password_validation.validate_password(attrs['password'])

        return attrs

    def create(self, data):

        data.pop('password_confirmation')
        user = User.objects.create_user(**data)

        return user
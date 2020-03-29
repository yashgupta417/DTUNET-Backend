from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.core import exceptions

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model=get_user_model()
        exclude=['last_login','following','is_active','is_admin','is_online']
        read_only=['is_online','u_id']
        extra_kwargs = {'password': {'write_only': True},
                        'name': {'write_only': True},
                        'email': {'write_only': True},
                        'image': {'write_only': True},
                        'label': {'write_only': True},
                        'bio': {'write_only': True},}

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)#The call to authenticate already checks that the user has the is_active flag
            if user==None:
                msg = ('Unable to log in with provided credentials')
                raise exceptions.ValidationError(msg)
        else:
            msg =('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        data['user'] = user
        return data

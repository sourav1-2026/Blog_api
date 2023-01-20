from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.Serializer):
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):

        """ Check the username is exist or not"""

        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Usename is already taken")
        return data

    def create(self, validated_data):
        user= User.objects.create(
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        username=validated_data['username'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()
        #print(**validated_data)
        return validated_data


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):

        """ Check the username is exist or not"""

        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("User not found")
        return data

    def get_tokens_for_user(self , data):
        #print("data {}".format(data))
        user= authenticate(username=data['username'],password=data['password'])
        print(user)

        if not user:
            return {'message':'invalid credentials','data':{}}
        
        # now we are generating token manually. 
        refresh = RefreshToken.for_user(user)
        return {
            'message':'login successfull',
            'data':{
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }
        }


    


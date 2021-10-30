from django.db import models
from django.db.models import fields
from rest_framework import serializers
from user.models import advisior_info
from django.contrib.auth.models import User

class advisior_info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = advisior_info
        # fields = '__all__'
        exclude = ['id',]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username= validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
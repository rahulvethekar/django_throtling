from dataclasses import fields
from signal import raise_signal
from rest_framework import serializers
from .models import Student,Employee
from django.contrib.auth.models import User


# class StudentSerializers(serializers.Serializer):
#     rn = serializers.IntegerField()
#     name = serializers.CharField()
#     city = serializers.CharField()
#     marks = serializers.IntegerField()


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_rn(self,value):
        if value > 50:
            raise serializers.ValidationError('admission full! ')
        return value


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    # email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']


    def validate_first_name(self,value):
        if len(value) > 20:
            raise serializers.ValidationError('Maximum 20 character is required')
        return value

    def create(self,validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

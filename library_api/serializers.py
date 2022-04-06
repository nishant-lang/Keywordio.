
from dataclasses import field
from rest_framework import serializers
from library_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""

    class Meta:
        model=models.UserProfile
        fields=('id','name','email','password')

        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user=models.UserProfile.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class AddBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AddBooks
        fields=('id','user_profile','book_name','crated_on')

        extra_kwargs={'user_profile':{'read_only':True}}

# class booklistSerializer(serializers.ModelSerializer):
#     class meta:
#         model=models.AddBooks
#         fields=('book_name')
from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

#Model Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object,
    se configura la Meta class para que el model serializer apunte a un modelo en especifico"""

    class Meta:
        model = models.UserProfile
         #List of fields that you want to manage through the serializer, los que quiero que sean accesibles o necesarios para create de API
        fields = ('id', 'email', 'name', 'password')
        # Como solo quiero password cuando creo usuario...
        extra_kwargs = {
            'password': {
                'write_only': True, #Only use it to create or update, not retrieve
                'style': {'input_type': 'password'} #To see dots when typing the password

            }
        }

    # Overrides the create function
    def create(self, validated_data):
         """Create and return a new user"""
         user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
         )

         return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields=('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True} }

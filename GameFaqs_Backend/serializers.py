from rest_framework import serializers
from GameFaqs_Backend import models
from django.contrib.auth import authenticate


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.GFUser
        fields = [
            'id',
            'username',
            'email',
            'signature',
            'website'
        ]


class CreateGFUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GFUser
        fields = ['id', 'username', 'password',
                  'signature', 'email', 'website']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = models.GFUser.objects.create_user(
            validated_data['username'],
            None,
            validated_data['password'],
            validated_data['signature'],
            validated_data['email'],
            validated_data['website']
        )
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to log in with provided credentials.")


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Game
        fields = [
            'id',
            'platform',
            'name',
            'esrb',
            'community_rating',
            'user_rating',
            'release_date'
        ]


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Platform
        fields = [
            'id',
            'consoles'
        ]


class FaqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Faq
        fields = [
            'id',
            'user',
            'game',
            'name',
            'body'
        ]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Message
        fields = [
            'id',
            'user',
            'title',
            'body',
            'datetime',
            'like',
            'game'
        ]

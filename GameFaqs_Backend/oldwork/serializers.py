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
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        user.signature = validated_data['signature']
        user.website = validated_data['website']
        user.save()
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
            'release_date',
            'console_name'
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
            'body',
            'game_name',
            'user_name'
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

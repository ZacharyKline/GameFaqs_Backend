from rest_framework.serializers import HyperlinkedModelSerializer
from GameFaqs_Backend import models


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.GFUser
        fields = [
            'id',
            'username',
            'email',
            'signature',
            'website'
        ]


class GameSerializer(HyperlinkedModelSerializer):
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


class PlatformSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Platform
        fields = [
            'id',
            'consoles'
        ]


class FaqSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Faq
        fields = [
            'id',
            'user',
            'game',
            'name',
            'body',

        ]


class MessageSerializer(HyperlinkedModelSerializer):
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

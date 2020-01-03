from rest_framework.serializers import HyperLinkedModelSerializer
from GameFaqs_Backend import models


class UserSerializer(HyperLinkedModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'id'
            'username',
            'email',
            'signature',
            'website'
        ]


class GameSerializer(HyperLinkedModelSerializer):
    class Meta:
        model = models.Game
        fields = [
            'id'
            'platform',
            'name',
            'ESRB_Rating',
            'com_rating',
            'user_rating',
            'faqs'
        ]


class PlatformSerializer(HyperLinkedModelSerializer):
    class Meta:
        model = models.Platform
        fields = [
            'id'
            'consoles'
        ]


class FaqSerializer(HyperLinkedModelSerializer):
    class Meta:
        model = models.Faq
        fields = [
            'id'
            'user',
            'game',
            'name',
            'body',

        ]


class MessageSerializer(HyperLinkedModelSerializer):
    class Meta:
        model = models.Message
        fields = [
            'id',
            'user',
            'title',
            'body',
            'datetime',
            'like'
        ]

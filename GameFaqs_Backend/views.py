from rest_framework import viewsets
from GameFaqs_Backend import models, serializers
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer


class FaqViewSet(viewsets.ModelViewSet):
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer

    @action(detail=True, methods=['get'])
    def uplike(self, request, pk=None):
        likes = models.Message.objects.get(pk=pk)
        likes.like += 1
        likes.save()
        return Response({'status': 'liked!'})

    @action(detail=True, methods=['get'])
    def downlike(self, request, pk=None):
        likes = models.Message.objects.get(pk=pk)
        likes.like -= 1
        likes.save()
        return Response({'status': 'unliked!'})

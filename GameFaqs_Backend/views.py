from rest_framework import viewsets, generics
from GameFaqs_Backend import models, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from knox.models import AuthToken

# from django.views.generic.edit import CreateView


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.GFUser.objects.all()
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


class LoginViewSet(generics.GenericAPIView):
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validate_data
        return Response({
            'user': serializers.UserSerializer(
                user,
                context=self.get_serializer_context()
            ).data,
            'token': AuthToken.objects.create(user)
        })


class RegistrationViewSet(generics.GenericAPIView):
    serializer_class = serializers.CreateGFUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.UserSerializer(
                user,
                context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })

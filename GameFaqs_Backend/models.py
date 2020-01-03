from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.PasswordField(min_length=6, max_length=40)
    signature = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    REQUIRED_FIELDS = ['username', 'password']


class Game(models.Model):
    pass


class Platform(models.Model):
    pass


class Faq(models.Model):
    pass


class Message(models.Model):
    post_time = models.DateTimeField(default=timezone.now)

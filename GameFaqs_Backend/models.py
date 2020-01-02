from django.db import models
from django.utils import timezone


class Game(models.Model):
    pass


class Platform(models.Model):
    pass


class Faq(models.Model):
    pass


class Message(models.Model):
    post_time = models.DateTimeField(default=timezone.now)

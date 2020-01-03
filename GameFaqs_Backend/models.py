from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model


class Game(models.Model):
    ESRB_CHOICES = [
        ("E","E"),
        ("T","T"),
        ("M", "M")
    ]

    platform = models.ForeignKey("Platform", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    community_rating = models.IntegerField()
    user_rating = models.IntegerField()
    # faqs = models.ForeignKey("Faq", on_delete=models.CASCADE)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    esrb = models.CharField(max_length=1, choices=ESRB_CHOICES)

    pass

class Platform(models.Model):
    Platform =  models.CharField(max_length=50)
    pass


class Faq(models.Model):
    user = models.ForeignKey(get_user_model(),
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    game = models.ForeignKey("Game", related_name = "game",null=True, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50, default="Steve")
    body = models.TextField()
    pass


class Message(models.Model):
    user = models.ForeignKey(get_user_model(),
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    body = models.TextField()
    like = models.BooleanField(default = False)
    post_time = models.DateTimeField(default=timezone.now)


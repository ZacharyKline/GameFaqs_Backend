from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import MinLengthValidator

# Minlength validator from stack overflow 
# https://stackoverflow.com/questions/2470760/django-charfield-with-fixed-length-how/
# 11952753
class GFUser(AbstractUser):
    # username = models.CharField(max_length=80, unique=True)
    signature = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    # USERNAME_FIELD = 'username'


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

    

class Platform(models.Model):
    consoles =  models.CharField(max_length=50)
    


class Faq(models.Model):
    user = models.ForeignKey(get_user_model(),
        # settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    game = models.ForeignKey("Game", related_name = "game",null=True, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50, default="Steve")
    body = models.TextField()
    


class Message(models.Model):
    user = models.ForeignKey(get_user_model(),
        # settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    body = models.TextField()
    like = models.BooleanField(default = False)
    datetime = models.DateTimeField(default=timezone.now)


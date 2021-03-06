from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model
# from django.conf import settings
# from django.core.validators import MinLengthValidator

# Minlength validator from stack overflow
# https://stackoverflow.com/questions/2470760/django-charfield-with-fixed-length-how/
# 11952753


class GFUser(AbstractUser):
    # username = models.CharField(max_length=80, unique=True)
    signature = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    # def get_absolute_url(self):
    #     return reverse('userdetail', kwargs={'id': self.id})

    def __str__(self):
        return f'{self.username}'


class Game(models.Model):
    ESRB_CHOICES = [
        ("E", "E"),
        ("T", "T"),
        ("M", "M")
    ]

    platform = models.ForeignKey("Platform", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    community_rating = models.IntegerField()
    user_rating = models.IntegerField()
    # faqs = models.ForeignKey("Faq", on_delete=models.CASCADE)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    esrb = models.CharField(max_length=1, choices=ESRB_CHOICES)

    def __str__(self):
        return f'{self.name} - {self.release_date}'

    @property
    def console_name(self):
        return self.platform.consoles


class Platform(models.Model):
    consoles = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.consoles}'


class Faq(models.Model):
    user = models.ForeignKey(get_user_model(),
                             # settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE
                             )
    game = models.ForeignKey("Game", related_name="game",
                             null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="Steve")
    body = models.TextField()
    post_time = models.DateTimeField(
        default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{self.game} - {self.name}'

    @property
    def game_name(self):
        return self.game.name

    @property
    def user_name(self):
        return self.user.username


class Message(models.Model):
    user = models.ForeignKey(get_user_model(),
                             # settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE
                             )
    title = models.CharField(max_length=50)
    body = models.TextField()
    like = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=timezone.now)
    game = models.ForeignKey("Game", related_name="gameify",
                             null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.title}'


class Question(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    # game = models.ForeignKey(Game ,on_delete=models.CASCADE)
    question_title = models.CharField(max_length=200)
    question_body = models.TextField(blank=True,null=True)
    datetime = models.DateTimeField(default=timezone.now)
    game = models.ForeignKey("Game", related_name="game_question", null=True, on_delete=models.CASCADE)
    answered = models.BooleanField(default=False, blank=True,null=True)
    spoiler = models.BooleanField(default=False, blank=True,null=True)


class Answer(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name="question_to_answer", on_delete=models.CASCADE)
    answer_body = models.TextField()
from django.contrib import admin
from django.contrib.auth.models import BaseUserManager
from GameFaqs_Backend import models


admin.site.register(models.GFUser)
admin.site.register(models.Game)
admin.site.register(models.Platform)
admin.site.register(models.Faq)
admin.site.register(models.Message)

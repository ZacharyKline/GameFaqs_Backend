from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from GameFaqs_Backend import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Game)
admin.site.register(models.Platform)
admin.site.register(models.Faq)
admin.site.register(models.Message)

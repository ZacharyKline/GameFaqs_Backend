"""GameFaqs_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from GameFaqs_Backend import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'platform', views.PlatformViewSet)
router.register(r'faq', views.FaqViewSet)
router.register(r'message', views.MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api/auth/', include('knox.urls')),
    url("^auth/register/$", views.RegistrationViewSet.as_view()),
    url("^auth/login/$", views.LoginViewSet.as_view()),




]

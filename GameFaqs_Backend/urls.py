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
from django.conf import settings
from django.conf.urls.static import static
from GameFaqs_Backend import views

urlpatterns = [
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logoutview, name='logoutview'),
    path('register/', views.register_user_view, name="registerview"),
    path('admin/', admin.site.urls, name='admin'),
    path('', views.ViewMainPage.as_view(), name='home'),
    path('game/<int:id>/', views.ViewGame.as_view(), name='gameview'),
    path('platform/<int:id>/',
         views.ViewConsole.as_view(), name='consoleview'),
    path('faq/<int:id>/', views.ViewFaqs.as_view(), name='faqview'),
    path('message/<int:id>/', views.ViewMessage.as_view(), name='messageview'),
    path('addfaq/<int:id>/', views.AddFaqView.as_view(), name='addfaq'),
    path('addmessage/<int:id>',
         views.AddMessageView.as_view(), name='addmessage'),
    path('allgames/', views.ViewAllGames.as_view()),
    path('allconsoles/', views.ViewAllConsoles.as_view()),
    path('allfaqs/', views.ViewAllFaqs.as_view()),
    path('addfaq/<int:id>/', views.AddFaqView.as_view()),
    path('addmessage/<int:id>', views.AddMessageView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

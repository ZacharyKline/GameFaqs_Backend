from GameFaqs_Backend.forms import LoginForm, RegisterForm
from GameFaqs_Backend.models import GFUser
from django.shortcuts import render, HttpResponseRedirect, reverse
from GameFaqs_Backend import models
from GameFaqs_Backend import forms
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
import logging


class ViewMainPage(View):
    def get(self, request):
        html = 'index.html'
        games = models.Game.objects.all()
        consoles = models.Platform.objects.all()
        return render(request, html, {'games': games, 'consoles': consoles})


class ViewGame(View):
    def get(self, request, id):
        html = 'games.html'
        games = models.Game.objects.get(id=id)
        faqs = models.Faq.objects.filter(game=games)
        return render(request, html, {'games': games, 'faqs': faqs})


class ViewConsole(View):
    def get(self, request, id):
        html = 'consoles.html'
        console = models.Platform.objects.get(id=id)
        games = models.Game.objects.filter(platform=console)
        return render(request, html, {'console': console, 'games': games})


class ViewFaqs(View):
    def get(self, request, id):
        html = 'faqs.html'
        game = models.Game.objects.get(id=id)
        faqs = models.Faq.objects.filter(game=game)
        return render(request, html, {'game': game, 'faqs': faqs})


def login_view(request):
    html = 'generic_form.html'
    page = 'login'
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('home'))
            )

    form = LoginForm()
    return render(request, html, {'form': form, 'page': page})


def register_user_view(request):
    html = 'generic_form.html'
    page = 'register'
    if request.method == "POST":

        form = forms.RegisterForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            u = GFUser.objects.create_user(
                username=data['username'],
                password=data['password'])

            login(request, u)
            return HttpResponseRedirect(reverse('home'))
    form = RegisterForm()
    return render(request, html, {'form': form, 'page': page})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))


class UserAccountView(TemplateView):
    template_name = "user_account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, pk, *args, **kwargs):
        my_user = models.GFUser.objects.get(pk=pk)
        user_faqs = models.Faq.objects.filter(user=my_user)
        
        return render(request, self.template_name, {"user_faqs": user_faqs} )
    

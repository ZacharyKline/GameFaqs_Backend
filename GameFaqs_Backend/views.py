from GameFaqs_Backend.forms import LoginForm, RegisterForm
from GameFaqs_Backend.models import GFUser
from django.shortcuts import render, HttpResponseRedirect, reverse
from GameFaqs_Backend import models
from GameFaqs_Backend import forms
from django.views import View
from django.contrib.auth import login, logout, authenticate


class ViewMainPage(View):
    def get(self, request):
        html = 'index.html'
        games = models.Game.objects.all()
        consoles = models.Platform.objects.all()
        return render(request, html, {'games': games, 'consoles': consoles})


class ViewGame(View):
    def get(self, request, id):
        html = 'games.html'
        data = models.Game.objects.filter(id=id)
        return render(request, html, {'data': data})


class ViewConsole(View):
    def get(self, request, id):
        html = 'consoles.html'
        data = models.Platform.objects.filter(id=id)
        return render(request, html, {'data': data})


class ViewFaqs(View):
    def get(self, request, game):
        html = 'faqs.html'
        data = models.Faq.objects.filter(game=game)
        return render(request, html, {'data': data})


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

            GFUser.objects.create(user=u)

            login(request, u)
            return HttpResponseRedirect(reverse('home'))
    form = RegisterForm()

    return render(request, html, {'form': form, 'page': page})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))

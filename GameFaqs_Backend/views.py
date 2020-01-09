from django.shortcuts import render, HttpResponseRedirect, reverse
from GameFaqs_Backend import models
from GameFaqs_Backend import forms
from django.views import View


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
    def get(self, request, id):
        html = 'faqs.html'
        data = models.Faq.objects.filter(id=id)
        return render(request, html, {'data': data})

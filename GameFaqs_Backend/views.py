from django.shortcuts import render, HttpResponseRedirect, reverse
from GameFaqs_Backend import models
from GameFaqs_Backend import forms
from django.views import View
from


class ViewMainPage(View):
    def get(self, request):
        html = 'index.html'
        games = models.Game.objects.all()
        consoles = models.Platform.objects.all()
        return render(request, html, {'games': games, 'consoles': consoles})


class ViewGame(View):
    def get(self, request, id):
        html = 'game.html'
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
@login_required
class AddFaqView(request, id):
    form = None
    html = "addfaq.html"
    if request.method =="POST":
        form = Add_FAQ(request.POST)

        if form.is_valid()
            data= form.cleaned_data
            Faq.objects.create(
            user=request.user,
            name=data['name'],
            body=data['body'],
            game=game.objects.get.filter.(id=id).first()
            )
        return redirect('/')
        else:
            return HttpResponseRedirect(reverse('/'))
    else:
        form = Add_FAQ()
    return render(request, html,{'form':form})

class AddMessageView(request, id):
    form = None
    html = addmessage.html
    if request.method == "POST":
        form = Add_Message(request.POST)

        if form.is_valid()
        data= form.cleaned_data
        Message.objects.create(
        user=request.user,
        title=data['title'],
        body=data['body'],
        game=game.objects.get.filter.(id=id).first()
        )
        return redirect('/')
        else:
            return HttpResponseRedirect(reverse('/'))
    else:
        form = Add_Message()
    return render(request, html, {'form':form})

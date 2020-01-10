from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
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
@method_decorator(login_required, name='dispatch')
class AddFaqView(View):
    html = "addfaq.html"
    form = forms.Add_FAQ
    def post(self, request):
        if request.method =="POST":
            form = Add_FAQ(request.POST)
            if form.is_valid():
                data= form.cleaned_data
            Faq.objects.create(
                user=request.user,
                name=data['name'],
                body=data['body'],
                game=models.Game.filter(id = id)
            )
            return redirect('/')
        else:
            return HttpResponseRedirect(reverse('/'))

    def get(self, request):
        form = Add_Faq()
        return render(request, self.html, {'form':form}) 

    
@method_decorator(login_required, name='dispatch')
class AddMessageView(View):
    html = "addmessage.html"
    form = forms.Add_Message
    def post(self, request, id):
        if request.method == "POST":
            form = forms.Add_Message(request.POST)

            if form.is_valid():
                data= form.cleaned_data
            models.Message.objects.create(
                user=request.user,
                title=data['title'],
                body=data['body'],
                game=models.Game.filter(id=id)
            )
            return redirect('/')
        else:
            return HttpResponseRedirect(reverse('/'))
    def get(self, request):
        form = forms.Add_Message()
        return render(request, self.html, {'form':form})

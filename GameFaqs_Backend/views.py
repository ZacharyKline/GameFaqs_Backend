from GameFaqs_Backend.forms import LoginForm, RegisterForm
from GameFaqs_Backend.models import GFUser
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
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
        games = models.Game.objects.get(id=id)
        faqs = models.Faq.objects.filter(game=games)
        messages = models.Message.objects.filter(game=games)
        return render(request, html, {'games': games, 'faqs': faqs, 'messages':messages})


class ViewConsole(View):
    def get(self, request, id):
        html = 'consoles.html'
        console = models.Platform.objects.get(id=id)
        games = models.Game.objects.filter(platform=console)
        return render(request, html, {'console': console, 'games': games})

# class ViewMessage(View):
#     def get(self, request, id):
#         html = "message.html"
#         user =  models.
#         game =  
#         name =  
#         body = 




class ViewFaqs(View):
    def get(self, request, id):
        html = 'faqs.html'
        data = models.Faq.objects.filter(id=id)
        return render(request, html, {'data': data})
@method_decorator(login_required, name='dispatch')
class AddFaqView(View):
    html = "addfaq.html"
    form = forms.Add_FAQ
    def post(self, request, id):
        # game_name = models.Game.objects.get(game=game)
        if request.method =="POST":
            form = forms.Add_FAQ(request.POST)
            if form.is_valid():
                data= form.cleaned_data
            # breakpoint()
            models.Faq.objects.create(
                user=request.user,
                name=data['name'],
                body=data['body'],
                game=data['game']
            )
            
            return HttpResponseRedirect(reverse('gameview', args=[id]))

    def get(self, request, id):
        instance = models.Game.objects.get(id=id)
        data = {'game':instance, 'name':'' ,'body':''}
        form = forms.Add_FAQ(initial=data)
        
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
                game=data['game']
            )
            return HttpResponseRedirect(reverse('gameview', args=[id]))
        # else:
    def get(self, request, id):
        instance = models.Game.objects.get(id=id)
        data = {'game':instance, 'title':'' ,'body':''}
        form = forms.Add_Message(initial=data)
        return render(request, self.html, {'form':form})



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

# def messagedetailview(request):
#     html = "messagedetail.html"


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

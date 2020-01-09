from django.shortcuts import render, HttpResponseRedirect, reverse
from GameFaqs_Backend import models
from GameFaqs_Backend.forms import LoginForm, RegisterForm
from GameFaqs_Backend.models import GFUser

def login_view(request):
    html = 'generic_form.html'
    page = 'login'
    if request.method == 'POST':
        form = LoginForm(request.POST)
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

        form = RegisterForm(request.POST)

        # already_a_user = User.objects.filter(username=current_user)

        # if already_a_user.exists():
        #     raise form.ValidationError("That user is already taken")

        if form.is_valid():

            data = form.cleaned_data

            u = User.objects.create_user(
                username=data['username'],
                password=data['password'])

            GFUser.objects.create(user=u)

            login(request, u)
            return HttpResponseRedirect(reverse('home'))
    form = RegisterForm()

    return render(request, html, {'form': form, 'page': page})


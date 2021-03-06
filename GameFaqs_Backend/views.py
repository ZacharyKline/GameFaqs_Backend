from GameFaqs_Backend.models import GFUser
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from GameFaqs_Backend import models, forms
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView


class ViewMainPage(View):
    def get(self, request):
        html = 'index.html'
        faqs = models.Faq.objects.all().order_by('-post_time')
        logged_in_user_id = request.user.id
        messages = models.Message.objects.all().order_by('-datetime')
        return render(request, html, {
            'faqs': faqs,
            'messages': messages,
            'logged_in_user_id': logged_in_user_id
        })


class ViewGame(View):
    def get(self, request, id):
        html = 'games.html'
        games = models.Game.objects.get(id=id)
        faqs = models.Faq.objects.filter(game=games).order_by('-post_time')
        messages = models.Message.objects.filter(
            game=games).order_by('-datetime')
        return render(
            request,
            html,
            {'games': games, 'faqs': faqs, 'messages': messages}
        )


class ViewConsole(View):
    def get(self, request, id):
        html = 'consoles.html'
        console = models.Platform.objects.get(id=id)
        games = models.Game.objects.filter(platform=console)
        return render(request, html, {'console': console, 'games': games})


class ViewMessage(View):
    def get(self, request, id):
        html = "message.html"
        data = models.Message.objects.filter(id=id)
        return render(request, html, {'data': data})


class ViewFaqs(View):
    def get(self, request, id):
        html = 'faqs.html'
        data = models.Faq.objects.filter(id=id)
        return render(request, html, {'data': data})


class ViewAllGames(View):
    def get(self, request):
        html = 'allgames.html'
        games = models.Game.objects.all()
        return render(request, html, {'games': games})


class ViewAllConsoles(View):
    def get(self, request):
        html = 'allconsoles.html'
        consoles = models.Platform.objects.all()
        return render(request, html, {'consoles': consoles})


class ViewAllFaqs(View):
    def get(self, request):
        logged_in_user_id = request.user.id
        html = 'allfaqs.html'
        faqs = models.Faq.objects.all()
        return render(request, html, {
            'faqs': faqs,
            'logged_in_user_id': logged_in_user_id
        })


@method_decorator(login_required, name='dispatch')
class AddFaqView(View):
    html = "addfaq.html"
    form = forms.Add_FAQ

    def post(self, request, id):
        # game_name = models.Game.objects.get(game=game)
        if request.method == "POST":
            form = forms.Add_FAQ(request.POST)
            if form.is_valid():
                data = form.cleaned_data

            models.Faq.objects.create(
                user=request.user,
                name=data['name'],
                body=data['body'],
                game=data['game']
            )
            return HttpResponseRedirect(reverse('gameview', args=[id]))

    def get(self, request, id):
        instance = models.Game.objects.get(id=id)
        data = {'game': instance, 'name': '', 'body': ''}
        form = forms.Add_FAQ(initial=data)
        return render(request, self.html, {'form': form})


@method_decorator(login_required, name='dispatch')
class AddMessageView(View):
    html = "addmessage.html"
    form = forms.Add_Message

    def post(self, request, id):
        if request.method == "POST":
            form = forms.Add_Message(request.POST)

            if form.is_valid():
                data = form.cleaned_data
            models.Message.objects.create(
                user=request.user,
                title=data['title'],
                body=data['body'],
                game=data['game']
            )
            return HttpResponseRedirect(reverse('gameview', args=[id]))

    def get(self, request, id):
        instance = models.Game.objects.get(id=id)
        data = {'game': instance, 'title': '', 'body': ''}
        form = forms.Add_Message(initial=data)
        return render(request, self.html, {'form': form})


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

    form = forms.LoginForm()
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
    form = forms.RegisterForm()
    return render(request, html, {
        'form': form,
        'page': page,
    })


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))


class UserAccountView(TemplateView):
    template_name = "user_account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, id, *args, **kwargs):
        my_user = models.GFUser.objects.get(id=id)
        user_faqs = models.Faq.objects.filter(user=my_user)
        user_messages = models.Message.objects.filter(user=my_user)

        return render(
            request,
            self.template_name,
            {
                "user_faqs": user_faqs,
                "my_user": my_user,
                'user_messages': user_messages
            }
        )


# class UserAccountEditView(UpdateView):
#     model = GFUser
#     fields = ['username', 'password', 'signature', 'website']
#     template_name= 'gfuser_update_form.html'

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid


def UserAccountEditView(request, id):
    html = 'gfuser_update_form.html'
    newUser = GFUser.objects.get(id=id)

    if request.method == "POST":
        form = forms.EditUserForm(request.POST, instance=newUser)
        form.save()
        return HttpResponseRedirect(reverse('userdetail', kwargs={'id': id}))

    form = forms.EditUserForm(instance=newUser)

    return render(request, html, {'form': form})



def QuestionView(request):
    html = 'question_page.html'
    all_questions = models.Question.objects.all()

    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        q = form.save(commit=False)
        q.user = request.user
        q.save()
        return HttpResponseRedirect(reverse('questionpage'))
        
    form = forms.QuestionForm()

    return render(request, html, {'form': form, 'question_list': all_questions})


def AnswerView(request, id):
    html = 'answers_page.html'

    the_question_to_answer = models.Question.objects.get(id=id)

    list_of_answers = models.Answer.objects.all()

    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        a = form.save(commit=False)
        a.user = request.user
        a.question = the_question_to_answer
        a.save()
        return HttpResponseRedirect(reverse('answerpage', kwargs={'id': id}))

    form = forms.AnswerForm()

    return render(request, html, {'form': form, 'answer_list': list_of_answers, 'question':the_question_to_answer})




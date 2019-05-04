from django.shortcuts import render, redirect
from .forms import WordForm
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Word
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Word
from django.contrib import messages
import re

def home(request):
    if request.user.is_authenticated:
        user = request.user
        get_word = Word.objects.filter(user=user).exists()
        if get_word:
            latest_word = Word.objects.filter(user=user).latest('id')
            return render(request, "notebook/home.html", {"word":latest_word})
    return render(request, "notebook/home.html")

@login_required
def query_words(request):
    return render(request, "notebook/query.html")

def search_user(request):
    return render(request, "notebook/search_user.html")

@login_required
def AddWord(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            messages.success(request, "A new word has been added successfully")
            return redirect('add-word')
    else:
        form = WordForm()
    return render(request, 'notebook/add-word.html', {'form':form} )

class WordListView(LoginRequiredMixin, ListView):
    model = Word
    template_name = 'notebook/mywords.html'
    paginate_by = 10
    def get_queryset(self):
        user = self.request.user
        return Word.objects.filter(user=user)

class UsersListView(LoginRequiredMixin, ListView):
    model = Word
    template_name = 'notebook/mywords.html'
    paginate_by = 10
    def get_queryset(self):
        username = self.request.GET.get('username')
        user = User.objects.filter(username__iexact=username)
        return Word.objects.filter(user__in=user)

class WordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Word
    template_name = 'notebook/updateword.html'
    fields = ['word','meaning','sentence','refrence']
    success_url =  '/wordslist/'

    def test_func(self):
        word = self.get_object()
        if self.request.user == word.user:
            return True
        return False

class WordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Word
    template_name = 'notebook/worddelete.html'
    success_url = '/wordslist/'

    def test_func(self):
        word = self.get_object()
        if self.request.user == word.user:
            return True
        return False

def get_word(request):
    word = request.GET.get('word')
    user = request.user
    queryset = Word.objects.filter(user=user, word__iexact=word).values()
    data = {
        "word" : list(queryset)
    }
    return JsonResponse(data)

def get_user(request):
    username = request.GET.get('username')
    user = User.objects.filter(username__icontains=username)
    queryset = user.values('username')
    data = {
        "user" : list(queryset)
    }
    if len(username) == 0:
        data['user'] = list()
    if user.exists():
        user_username_inqueryset = User.objects.filter(username=queryset[0]['username'])
        image = user_username_inqueryset.first().profile.image.url
        data['image'] = image
    return JsonResponse(data)

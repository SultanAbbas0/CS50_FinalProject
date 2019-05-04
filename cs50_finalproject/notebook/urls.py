"""cs50_finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import home, AddWord, WordListView, WordUpdateView, WordDeleteView, query_words, search_user, UsersListView

urlpatterns = [
    path('', home, name="home-page"),
    path('add/', AddWord, name="add-word"),
    path('wordslist/', WordListView.as_view() , name="my-words"),
    path('userwordslist/', UsersListView.as_view() , name="user-words"),
    path('wordupdate/<int:pk>', WordUpdateView.as_view() , name="word-update"),
    path('worddelete/<int:pk>', WordDeleteView.as_view() , name="word-delete"),
    path('query/', query_words, name="query_words"),
    path('users/', search_user, name="search_user"),
]

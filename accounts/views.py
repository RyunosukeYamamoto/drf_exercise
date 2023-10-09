from typing import Any
from django import http
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Articles, User
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import ArticleForm, UserForm


# Create your views here.
class ArticleList(ListView):
    model = Articles
    template_name = "article_list.html"


class ArticleCreate(CreateView):
    template_name = "article_create.html"
    form_class = ArticleForm
    success_url = "/app/index/"

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super().form_valid(form)


class UserCreate(CreateView):
    template_name = "user_create.html"
    form_class = UserForm
    success_url = "/app/login/"


class UserList(ListView):
    model = User
    template_name = "user_list.html"

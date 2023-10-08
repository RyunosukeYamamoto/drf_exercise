from typing import Any
from django import forms
from .models import Articles, User


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        exclude = ["user"]

    # def save(self, commit=False):
    #     article = super().save(commit)
    #     article.user = self.request.user
    #     article.save()
    #     return article

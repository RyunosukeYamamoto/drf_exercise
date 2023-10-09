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


class UserForm(forms.ModelForm):
    icon = forms.ImageField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(), label="パスワード")

    class Meta:
        model = User
        fields = ["email", "username", "password", "icon", "is_superuser", "is_staff"]

    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        user.save()
        return user

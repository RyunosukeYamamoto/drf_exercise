from django.urls import path
from accounts import views
from .views import ArticleList, ArticleCreate
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    path("index/", ArticleList.as_view(), name="index"),
    path("create/", ArticleCreate.as_view(), name="create"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

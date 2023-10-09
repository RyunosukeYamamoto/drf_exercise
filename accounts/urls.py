from django.urls import path
from accounts import views
from .views import ArticleList, ArticleCreate, UserCreate, UserList
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    path("index/", ArticleList.as_view(), name="index"),
    path("user_index/", UserList.as_view(), name="user_index"),
    path("create/", ArticleCreate.as_view(), name="create"),
    path("signup/", UserCreate.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

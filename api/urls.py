from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken import views as auth_views
from .auth import CustomAuthToken

# router = routers.DefaultRouter()
# router.register(r"articles", views.ArticleViewSet)

urlpatterns = [
    # path("", include(router.urls)),
    path("articles/", views.ArticleAPIlistCreate.as_view()),
    path("articles/<int:pk>/", views.ArticleAPIRetrieveUpdateDestroy.as_view()),
    path("create_token/", CustomAuthToken.as_view()),
]

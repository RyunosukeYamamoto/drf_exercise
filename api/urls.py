from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken import views as auth_views

router = routers.DefaultRouter()
router.register(r"articles", views.ArticleViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("create_token/", auth_views.obtain_auth_token),
]

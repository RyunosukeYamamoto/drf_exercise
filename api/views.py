from rest_framework import viewsets, status
from accounts.models import Articles
from .serializers import ArticleSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from django.http import Http404


class ArticleAPIlistCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     response.data["user"] = self.request.user.pk
    #     return response


class ArticleAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

    # def get_object(self):
    #     try:
    #         instance = self.queryset.filter(pk=self.kwargs["pk"], user=self.request.user)
    #         return instance
    #     except Articles.DoesNotExist:
    #         raise Http404

    def destroy(self, request, pk, *args, **kwargs):
        article = Articles.objects.filter(pk=pk, user=self.request.user)
        if article:
            return super().destroy(request, pk, *args, **kwargs)
        else:
            raise Http404

    def update(self, request, pk, *args, **kwargs):
        article = Articles.objects.filter(pk=pk, user=self.request.user)
        if article:
            return super().update(request, pk, *args, **kwargs)
        else:
            raise Http404

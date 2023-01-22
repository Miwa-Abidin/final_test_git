from rest_framework import viewsets

from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
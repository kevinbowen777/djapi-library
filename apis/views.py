from django.contrib.auth import get_user_model
from rest_framework import viewsets

from books.models import Book
from .permissions import IsAuthorOrReadOnly
from .serializers import BookSerializer, UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

from rest_framework import generics

from books.models import Book
from .permissions import IsAuthorOrReadOnly
from .serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

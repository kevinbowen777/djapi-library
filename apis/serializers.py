from books.models import Book
from django.contrib.auth import get_user_model
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "subtitle",
            "author",
            "pages",
            "publisher",
            "pubdate",
            "price",
            "isbn",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "email",
        )

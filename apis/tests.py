from books.models import Book
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django for APIs",
            subtitle="Build web APIs with Python and Django",
            author="William S. Vincent",
            pages="200",
            publisher="Lean Publishing",
            pubdate="2022-04-01",
            price="29.99",
            isbn="9781735467221",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("book_detail", kwargs={"pk": self.book.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, "Build web APIs")

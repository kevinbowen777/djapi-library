from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book


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
        cls.user = get_user_model().objects.create_user(
            username="bookreader",
            password="T3stP@s5123",
        )

    def test_api_listview(self):
        self.client.login(username="bookreader", password="T3stP@s5123")
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)

    def test_api_logged_out_deny_listview_access(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_detailview(self):
        self.client.login(username="bookreader", password="T3stP@s5123")
        response = self.client.get(
            reverse("book_detail", kwargs={"pk": self.book.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, "Build web APIs")

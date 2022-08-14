from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Code Complete",
            subtitle="A handbook of software construction",
            author="Steve McConnell",
            pages="952",
            publisher="Microsoft Press",
            pubdate="2004-03-29",
            price="65.72",
            isbn="0735619670",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Code Complete")
        self.assertEqual(
            self.book.subtitle, "A handbook of software construction"
        )
        self.assertEqual(self.book.author, "Steve McConnell")
        self.assertEqual(self.book.pages, "952")
        self.assertEqual(self.book.publisher, "Microsoft Press")
        self.assertEqual(self.book.pubdate, "2004-03-29")
        self.assertEqual(self.book.price, "65.72")
        self.assertEqual(self.book.isbn, "0735619670")

    def test_book_listview(self):
        response = self.client.get(reverse("booklist"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A handbook of software construction")
        self.assertTemplateUsed(response, "books/book_list.html")

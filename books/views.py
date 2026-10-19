from typing import ClassVar

from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

    ordering: ClassVar[list[str]] = ["title"]
    paginate_by = 2

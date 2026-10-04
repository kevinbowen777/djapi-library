from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

    ordering = ["title"]
    paginate_by = 2

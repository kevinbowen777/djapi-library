from books.views import BookListView
from django.urls import path

from .views import AboutPageView, HomePageView


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("books/", BookListView.as_view(), name="booklist"),
]

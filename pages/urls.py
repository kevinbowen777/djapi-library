from django.urls import path

from books.views import BookListView

from .views import (
    AboutPageView,
    ContactView,
    HomePageView,
    SuccessView,
)

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactView, name="contact"),
    path("success/", SuccessView, name="success"),
    path("", HomePageView.as_view(), name="home"),
    path("books/", BookListView.as_view(), name="booklist"),
]

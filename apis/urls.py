from django.urls import path

from .views import BookList, BookDetail, UserList, UserDetail


urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("", BookList.as_view(), name="book_list"),
    path("<int:pk>/", BookDetail.as_view(), name="book_detail"),
]

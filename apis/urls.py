from django.urls import path

from .views import BookAPIView, BookAPIDetailView


urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list"),
    path("<int:pk>/", BookAPIDetailView.as_view(), name="book_detail"),
]

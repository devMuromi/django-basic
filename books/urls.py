from django.urls import path
from books import views

urlpatterns = [path("books/", views.books, name="books"), path("books/<int:book_id>", views.book)]

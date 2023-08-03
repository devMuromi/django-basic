from django.urls import path
from books import views

app_name = "books"
urlpatterns = [
    path("", views.books, name="books"),
    path("<int:book_id>/", views.book_detail, name="book_detail"),
    path("create/", views.create_book, name="create_book"),
]

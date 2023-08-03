from django.http import HttpResponse
from books.models import Book

from django.shortcuts import render

# from django.template import loader


def books(request):
    books = Book.objects.all()
    context = {
        "book_list": books,
    }
    return render(request, "books/index.html", context)
    # template = loader.get_template("books/index.html")
    # return HttpResponse(template.render(context, request))


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return HttpResponse(f"{book.title} / {book.author.name}")


def create_book(request):
    Book.objects.create(title="빙과", page_count=256, author_id=1)
    return HttpResponse("책 생성 완료")

from django.http import HttpResponse
from books.models import Book


def books(request):
    books = Book.objects.all()
    res = ""
    for book in books:
        res += f"{book.title} / {book.author.name}<br>"
    return HttpResponse(res)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return HttpResponse(f"{book.title} / {book.author.name}")


def create_book(request):
    Book.objects.create(title="빙과", page_count=256, author_id=1)
    return HttpResponse("책 생성 완료")

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True)


class Book(models.Model):
    title = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    page_count = models.IntegerField(null=True)

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    summary = models.TextField(max_length=255)
    genre = models.CharField(max_length=255)
    publish_date = models.DateField()



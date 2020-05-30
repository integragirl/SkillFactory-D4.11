from django.db import models
from decimal import Decimal

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name + ' ' + str(self.country)

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField(verbose_name='Название')
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('1.00'))

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class PublisherBook(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='pb_publisher')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pb_book')

    def __str__(self):
        return str(self.publisher) + ' - ' + str(self.book)
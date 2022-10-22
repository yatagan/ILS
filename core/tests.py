from django.test import TestCase

from core.models import Book, BookInstance, Author

# class BookInstanceCase(TestCase):
#     fixtures = ['core/fixtures/library.yaml',]

#     def test_number_books(self):
#         """Animals that can speak are correctly identified"""

#         books = Book.objects.filter(title__contains='Head first')
#         book = books[0]

#         BookInstance.objects.create(book=book)
#         BookInstance.objects.create(book=book)

#         self.assertEqual(book.number_books(), 2)

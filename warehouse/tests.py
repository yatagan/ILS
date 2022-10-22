from django.test import TestCase, Client
from django.urls import reverse
from core.models import Author, Book, BookInstance
from warehouse.models import Rack
from visitors.models import Librarian


class AccessTestCase(TestCase):
    def test_anonymous_cant_see_warehouse(self):
        c = Client()

        index_resp = c.get(reverse('warehouse:index'))
        self.assertNotEqual(index_resp.status_code, 200)

        add_book_resp = c.get(reverse('warehouse:add_book_instance'))
        self.assertNotEqual(add_book_resp.status_code, 200)

        post_add_book_resp = c.post(
            reverse('warehouse:add_book_instance'),
            {}
        )
        self.assertNotEqual(post_add_book_resp.status_code, 200)


class AddBookInstanceTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Ukraine is not Russia"
        )

        self.rack = Rack.objects.create(title="Politics")

        self.c = Client()
        self.c.force_login(
            Librarian.objects.create(
                username='librarian', 
                password='password', 
                # TODO: remove
                is_staff=True
            )
        )

    def test_success_addition(self):
        number = 10
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': 'm',
                'format_book': 1,
                'number': number,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )

        self.assertEqual(response.status_code, 302)
        
        # check book items exist
        self.assertEqual(
            BookInstance.objects.all().count(),
            number
        )

        # check the book items are on the rack
        # Rack.objects.get(id=rack.id)
        self.assertEqual(
            BookInstance.objects.all().count(),
            self.rack.books.count()
        )


    def test_book_not_exist(self):
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': 2222,
                'status': 'm',
                'format_book': 1,
                'number': 1,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )
        self.assertNotEqual(response.status_code, 302)
    
    def test_rack_not_exist(self):
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': 'm',
                'format_book': 1,
                'number': 1,
                'isbn': 'ISBN',
                'rack': 3333,
            },
        )
        self.assertNotEqual(response.status_code, 302)

    def test_not_required_fields(self):
        # no book
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'status': 'm',
                'format_book': 1,
                'number': 1,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )
        self.assertNotEqual(response.status_code, 302)

        # no status
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'status': 'm',
                'format_book': 1,
                'number': 1,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )
        self.assertNotEqual(response.status_code, 302)
        self.assert_(BookInstance.objects.all().count() == 0)

        # no format
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': 'm',
                'number': 1,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )
        self.assertNotEqual(response.status_code, 302)
        self.assert_(BookInstance.objects.all().count() == 0)

        # no number
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': 'm',
                'format_book': 1,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )
        self.assertNotEqual(response.status_code, 302)
        self.assert_(BookInstance.objects.all().count() == 0)

        # no isbn
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': 'm',
                'format_book': 1,
                'number': 1,
                'rack': self.rack.id,
            },
        )
        self.assertNotEqual(response.status_code, 302)
        self.assert_(BookInstance.objects.all().count() == 0)

        # no rack
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': 'm',
                'format_book': 1,
                'number': 1,
                'isbn': 'ISBN',
            },
        )
        self.assertNotEqual(response.status_code, 302)
        self.assert_(BookInstance.objects.all().count() == 0)


    def test_wrong_number(self):
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': 'm',
                'format_book': 1,
                'number': 0,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )
        self.assert_(BookInstance.objects.all().count() == 0)

        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': 'm',
                'format_book': 1,
                'number': -10,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )
        self.assert_(BookInstance.objects.all().count() == 0)

    def test_book_format(self):
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': 'm',
                'format_book': 2,
                'number': 1,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )
        self.assertEqual(response.status_code, 302),
        self.assertEqual(
            BookInstance.objects.all().count(), 1
        )
        book_instanse = BookInstance.objects.get(book=self.book)
        self.assert_(book_instanse.format_book == 2)

    def test_book_status(self):
        expected_status = 'a'
        response = self.c.post(
            reverse('warehouse:add_book_instance'),
            {
                'book': self.book.id,
                'status': expected_status,
                'format_book': 2,
                'number': 1,
                'isbn': 'ISBN',
                'rack': self.rack.id,
            },
        )
        self.assertEqual(response.status_code, 302),
        self.assertEqual(
            BookInstance.objects.all().count(), 1
        )
        book_instanse = BookInstance.objects.get(book=self.book)
        self.assertEqual(book_instanse.status, expected_status)
from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from core.models import Author, Book, BookInstance
from visitors.models import Account, Member, Librarian
from library_reception.models import BookInstanceRent

# TestBookCheckOut

# Створити книжки, екземпляри
# Створити користувачів
#     * незареєствованим
#     * Member
#     * Librarian
#     * Admin

class BookCheckOutTestCase(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(title="Book #1")
        
        BookInstance.objects.create(book=self.book1, format_book=1)

        User.objects.create(username='admin', password='password')
        self.member = Member.objects.create(username='member', password='password')
        self.librarian = Librarian.objects.create(username='librarian', password='password')
        ...

    def test_anonymous_journal(self):
        c = Client()
        response = c.get('/library_reception/')
        self.assertContains(response, "Журнал")

    def test_anonymous_try_checkout(self):
        c = Client()
        response = c.get(reverse('library_reception:book_rent'))
        self.assertEqual(response.status_code, 401)

    def test_anonymous_checkout(self):
        c = Client()
        response = c.post(
            reverse('library_reception:book_rent'),
            {
                'books': (self.book1.id), 
                'member': self.member.id,
                'library': self.librarian.id,
                'start_rent_date': datetime.now(),
                'return_date': datetime.now(),
            }
        )
        response = c.get('/library_reception/')
        
        self.assertContains(response, "Журнал арендованих книг")
        self.assertEquals(BookInstanceRent.objects.all().count(), 1)

    # def test_checkout_by_admin(self):

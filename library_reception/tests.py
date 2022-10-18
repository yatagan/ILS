from datetime import datetime
from urllib import response
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
        
        self.book_instance = BookInstance.objects.create(book=self.book1, format_book=1, status='a')

        self.admin = User.objects.create(username='admin', password='password')
        self.member = Member.objects.create(username='member', password='password')
        self.librarian = Librarian.objects.create(username='librarian', password='password')


    def test_reject_anonymous_journal(self):
        c = Client()
        response = c.get('/library_reception/')
        self.assertNotEqual(response.status_code, 200)


    def test_reject_anonymous_book_rent(self):
        c = Client()
        response = c.get(reverse('library_reception:book_rent'))
        self.assert_(self._is_redirected_to_login(response))


    def test_reject_anonymous_checkout(self):
        c = Client()
        response = self._post_book_rent(c, follow=False)
        self.assert_(self._is_redirected_to_login(response))


    def test_reject_member_checkout(self):
        c = Client()
        c.force_login(self.member)
        response = self._post_book_rent(c)
        self.assertEqual(response.status_code, 401)


    def test_reject_admin_checkout(self):
        c = Client()
        c.force_login(self.admin)
        response = self._post_book_rent(c)
        self.assertEqual(response.status_code, 401)
        self.assertEquals(BookInstanceRent.objects.all().count(), 0)

    def test_librarian_checkout(self):
        c = Client()
        c.force_login(self.librarian)
        response = self._post_book_rent(c)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Журнал арендованих книг")
        self.assertEquals(BookInstanceRent.objects.all().count(), 1)

    def test_bookinstance_return(self):
        c=Client()
        c.force_login(self.librarian)
        response = self._post_bookinstance_return(c)
        self.assertEqual(response.status_code, 200)
          

    def _post_book_rent(self, client, follow=True):
        now = datetime.now()
        return client.post(
            reverse('library_reception:book_rent'),
            {
                'books': (self.book_instance.id), 
                'member': self.member.id,
                'librarian': self.librarian.id,
                
                'start_rent_date_month': now.month,
                'start_rent_date_day': now.day,
                'start_rent_date_year': now.year,

                'return_date_month': now.month,
                'return_date_day': now.day,
                'return_date_year': now.year,
            },
            follow=follow,
        )

    def _is_redirected_to_login(self, response):
        return response.status_code == 302 and 'login' in response.url

    def _post_bookinstance_return(self, client, follow=True):
        now_time = datetime.now()
        return client.post(
            reverse('warehouse:return_instance'),
            {
                'id': (self.book_instance.id),
                'librarian': (self.librarian.id),

                'date_return_month': now_time.month,
                'return_date_day': now_time.day,
                'return_date_year': now_time.year,
            },
            follow=follow,
        )    

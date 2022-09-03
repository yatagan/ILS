from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _


class Account(auth_models.User):

    class AccountStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Active')
        CLOSED = 'CLOSED', _('Closed')
        CANCELED = 'CANCELED', _('Canceled')
        BLACKLISTED = 'BLACKLISTED', _('Blacklisted')
        NONE = 'None', _('None')

    status = models.CharField(
        max_length=32,
        choices=AccountStatus.choices,
        default=AccountStatus.NONE,
    )


class Librarian(Account):

    class Meta:
        verbose_name = 'Librarian'
        verbose_name_plural = 'Librarians'

    def addBookItem(self, book):
        ...


class Member(Account):

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    totalBooksCheckedout = models.IntegerField(default=0)

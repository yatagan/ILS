# ТЗ
https://www.educative.io/courses/grokking-the-object-oriented-design-interview/RMlM3NgjAyR

   ./manage.py migrate
   ./manage.py loaddata admins library


# Система керування бібліоткекою

* Головна сторінка бібліотеки (Контакти, історія, новини) (https://mylib.ua/)
* Адмінка бабушкі в читальному залі (https://mylib.ua/chitalka)
* Адмінка зав. складу (https://mylib.ua/warehouse)
* Адмінка Django
  * Форма додавання Авторів
  * Форма додавання Книжок

## Головна
  * Новинки
  * Контакти
  * Пошук по книжкам

## Склад
  * Форма додавання екземплярів книжок
    * Книжка
    * *ISBN (http://www.ukrbook.net/agentstvo.html)*
    * Кількість

## Library reception
  * Форма видачі книжки(ок)
    * Екземпляки книжок, що бере клієнт
    * Клієнт
    * Дата
    How do I see realisation for this:
    - VISITOR coming to reception - REGISTRATION or LOG IN
    - formation NEW_ORDER - (name_book, autor, availability check)
    - formation CARD_RENT - (name_book, autor, visitor, data_rent_on, data_rent_off)
    - may be: if data_rent_off is comming - send message to e-mail


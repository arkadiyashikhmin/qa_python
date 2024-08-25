import pytest
from main import BooksCollector

class TestBooksCollector:
    # тест для проверки, что добавились именно 2 книги
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # тест для проверки добавления книги в избранное
    def test_add_book_in_favorites_positive_result(self):
        collector = BooksCollector()

        collector.books_genre = {'Гарри Поттер': 'Фантастика'}
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    # тест для проверки удаления из избранного
    def test_delete_book_from_favorites_positive_result(self):
        collector = BooksCollector()

        collector.favorites = ['Гарри Поттер']
        collector.delete_book_from_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []

    # тест для проверки, что в избранном содержатся добавленные книги
    def test_get_list_of_favorites_books_positive_result(self):
        collector = BooksCollector()

        collector.favorites = ['Властелин колец', 'Пока не сыграл в ящик']
        assert len(collector.get_list_of_favorites_books()) == 2

    # тест для проверки, что книга с названием более 40 символов не добавляется
    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()

        collector.add_new_book('Особенности национальной подледной ловли, или Отрыв по полной')
        assert collector.get_books_genre() == {}

    # тест для проверки соответствия детских книг для детей
    def test_get_books_for_children_positive_result(self):
        collector = BooksCollector()

        collector.books_genre = {
                                 'Обливион': 'Ужасы',
                                 'Ну погоди': 'Мультфильмы'}

        assert collector.get_books_for_children() == ['Ну погоди']

    # тест для проверки что в случае двух книг с одинаковым названием, добавляется только одна
    def test_add_new_book_again(self):
        collector = BooksCollector()

        book_name = 'Пособие ГИБДД'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

        # тест для проверки, что в словаре отображаются все добавленные книги
    def test_get_books_genre_positive_resilt(self):
            collector = BooksCollector()

            collector.books_genre = {'Гарри Поттер': 'Фантастиика',
                                     'Ну погоди': 'Мультфильмы',
                                     'Обливион': 'Ужасы'}

            assert collector.get_books_genre() == {'Гарри Поттер': 'Фантастиика',
                                                   'Ну погоди': 'Мультфильмы',
                                                   'Обливион': 'Ужасы'}

    # несуществуюший жанр не добавляется к названию книги
    def test_set_book_genre_add_not_incorrect_genre(self):
        collector = BooksCollector()

        book = 'Достать ножи'
        collector.add_new_book(book)
        genre = 'Многосерийный'
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == ''

    # тест проверяет, что длина списка книг по жанру соответствуюет количеству
    def test_get_books_with_specific_genre_positive_result(self):
        collector = BooksCollector()

        genre = 'Ужасы'
        books = ['Обливион', 'Зеркала', 'Давай поженимся']

        for book_name in books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        assert len(collector.get_books_with_specific_genre(genre)) == len(books)
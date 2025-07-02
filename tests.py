import pytest
class TestBooksCollector:

    def test_books_genre_fav_dict_is_empty(self, books_collector): #тест проверяет словари конструтора при создании объекты

        assert len(books_collector.books_genre) == 0 and len(books_collector.favorites) == 0

    def test_genre_list_is_not_empty(self, books_collector): #проверка что у созданного объекта есть список со жанрами

        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_list_is_not_empty(self, books_collector): #провера что у созданного объекта есть список со жанрами 18+

        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('book', ['Мальчик с пальчик', 'Барабашка']) #параметризация проверяет добавление новых книг в список
    def test_add_new_book_positive(self, books_collector, book):

        books_collector.add_new_book(book)
        assert books_collector.books_genre[book] == ''

    @pytest.mark.parametrize('book', ['', 'Когда на землю спускается закат, они всегда просыпаются к ночи']) #параметризация, проверка что книги с 40+ символами не добавляются в список книг
    def test_add_new_book_more_negative_sizes(self, books_collector, book):

        assert not books_collector.add_new_book(book)

    def test_set_book_genre_valid_name(self, books_collector):# проверка добавления новых книг с корректным названием и присвоение книгам жанра

        books_collector.add_new_book('Агата не дремлет')
        books_collector.set_book_genre('Агата не дремлет', 'Детективы')
        assert books_collector.books_genre['Агата не дремлет'] == 'Детективы'

    @pytest.mark.parametrize('name, genre', [
        ['Ночной экспресс не приедет, так как он уехал в другой мир', 'Детективы'],
        ['Чудное озеро', 'Небылица'] #параметризация, создается список из добавляемых книг, где одна книга не добавляется из-за размера названия, а вторая добавляется, но имеет невалидный жанр.
    ])
    def test_set_book_genre_negative_case(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.set_book_genre(name, genre)

    def test_get_book_genre_return_valid_name(self, books_collector): #проверка возвращения жанра книги по названию. Добавляем книгу, задаем жанр, проверяем что жанр по названию выводится верно.

        books_collector.add_new_book('Винни пух в космосе')
        books_collector.set_book_genre('Винни пух в космосе', 'Фантастика')
        assert books_collector.get_book_genre('Винни пух в космосе') == 'Фантастика'

    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):# проверка что выводится список по жанрам. Добаялаем книу, задаем жанр, проверяем жанр и что список книг ему соответствует.

        books_collector.add_new_book('Буратино')
        books_collector.set_book_genre('Буратино', 'Мультфильмы')
        assert books_collector.get_books_with_specific_genre('Мультфильмы') \
               and type(books_collector.get_books_with_specific_genre('Мультфильмы')) == list

    @pytest.mark.parametrize('name, genre', [['', 'Фантастика'], ['Чарли Чаплин', 'Комедии']]) #параметризация- добавляем книги и пробуем получить список по жанру. Нельзя получить список по невалидному жанру или если список пустой.
    def test_get_books_with_specific_genre_empty_list_book_false_genre(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.get_books_with_specific_genre('Рассказ')

    def test_get_books_genre_empty_dict(self, books_collector): #проверка что нельзя получить пустой список

        assert not books_collector.get_books_genre()

    def test_get_books_for_children_correct_genre(self, books_collector): #проверка что в списке есть только книги для детей. Циклом создаем список и добавляем разные жанры. Вторым циклом проверяем есть ли в первом списке книги 18+.

        books = ['Лабубу', 'Первое или второе', 'Окончание', 'Василий меняет профессию', 'Ладья']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1

        for rating in books_collector.genre_age_rating:
            assert rating not in books_collector.get_books_for_children()

    def test_get_books_for_children_adult_rating(self, books_collector): #проверяем что книги 18+ не попадают в список книг для детей.

        books = ['Дюймовочка', 'Снежная королева']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre_age_rating[x])
            x += 1

        assert not books_collector.get_books_for_children()

    def test_add_book_in_favorites_when_books_in_list(self, books_collector):#проверяем что книга, добавленная в избранное есть в избранном.

        books_collector.add_new_book('Гарри Поттер')
        books_collector.add_book_in_favorites('Гарри Поттер')

        assert 'Гарри Поттер' in books_collector.favorites

    def test_add_book_in_favorites_when_book_not_in_list(self, books_collector):#проверяем что нельзя книгу добавить в избранное, если её нет в списке книг.

        books = ['Властелин колец', 'Маленький мук', 'Бражник'] #добавляем книги в список и затем в избранное
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert not books_collector.add_book_in_favorites('Мцыри') #пытаемся добавить книгу не из списка в избранное

    def test_delete_book_from_favorites(self, books_collector):#проверяем возможность удаления книги из избранного

        books_collector.add_new_book('Знамение')
        books_collector.add_book_in_favorites('Знамение')

        books_collector.delete_book_from_favorites('Знамение')
        assert 'Знамение' not in books_collector.favorites

    def test_delete_book_from_favorites_no_name_in_list(self, books_collector): #проверка возможности удаления книги из избранного, которой в избранном нет

        books_collector.add_new_book('Муха в шоколаде')
        books_collector.add_book_in_favorites('Муха в шоколаде')

        assert not books_collector.delete_book_from_favorites('Заяц и волк')

    def test_get_list_of_favorites_books_not_empty(self, books_collector):#проверяем корректность метода, который выводит список книг в избранном

        books = ['Преступление и наказание', 'Крик', 'Папа купил автомобиль']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty_list(self, books_collector):#проверка что если книгу добавить в избранное, потом удалить, то список избранного будет пустым

        books_collector.add_new_book('Бемби')
        books_collector.add_book_in_favorites('Бемби')
        books_collector.delete_book_from_favorites('Бемби')

        assert not books_collector.get_list_of_favorites_books()
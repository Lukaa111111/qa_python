Описание тестовых функций для класса BooksCollector:


1. Проверяет словари конструктора при создании объекта
    def test_books_genre_fav_dict_is_empty(self, books_collector):

        assert len(books_collector.books_genre) == 0 and len(books_collector.favorites) == 0

2. Проверяет что у созданного объекта есть заполненный список с жанрами
    def test_genre_list_is_not_empty(self, books_collector):

        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

3. Проверяет что у созданного объекта есть список с жанрами 18+
    def test_genre_age_rating_list_is_not_empty(self, books_collector):

        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']  

4. Тест с параметризацией проверяет добавление новых книг в список
    @pytest.mark.parametrize('book', ['Мальчик с пальчик', 'Барабашка'])
    def test_add_new_book_positive(self, books_collector, book):
        books_collector.add_new_book(book)
        assert books_collector.books_genre[book] == ''

5.Тест проверяет что книги с названиями 40+ символов не будут добавлены в список книг
    @pytest.mark.parametrize('book', ['', 'Когда на землю опускается закат, они всегда просыпаются к ночи'])
    def test_add_new_book_more_negative_sizes(self, books_collector, book):
        assert not books_collector.add_new_book(book)

6. Тест с параметризацией добавляет новые книги и проверяет задавание книгам жанров
    @pytest.mark.parametrize('name, genre', [
        ['Пирамидо-сосковая война', 'Детективы'],
        ['Мастер и Минотавр', 'Ужасы']

7. Тест проверяет возможность добавления новых книг с корректным названием и присвоение книгам жанра
    def test_set_book_genre_valid_name(self, books_collector, name, genre):

        books_collector.add_new_book('Агата не дремлет')
        books_collector.set_book_genre('Агата не дремлет', 'Детективы')
        assert books_collector.books_genre['Агата не дремлет'] == 'Детективы'

8.Тест проверяет возсожность добвления книг с некорректными параметрами. Создается список из добавленных книг, где первая не добавляется из-за размера, а вторая добавляется, но имеет невалидный жанр.
    @pytest.mark.parametrize('name, genre', [
        ['Ночной экспресс не приедет, так как он уехал в другой мир', 'Детективы'],
        ['Чудное озеро', 'Небылица']
    ])
    def test_set_book_genre_negative_case(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.set_book_genre(name, genre)

9. Тест проверяет возвращение жанра книги по названию. Добавляем книгу, задаем жанр. Проверяется что по названию возвращается жанр.
    def test_get_book_genre_return_valid_name(self, books_collector):

        books_collector.add_new_book('Винни пух в космосе')
        books_collector.set_book_genre('Винни пух в космосе', 'Фантастика')
        assert books_collector.get_book_genre('Винни пух в космосе') == 'Фантастика'

10.Тест проверяет что выводится список книг по определенным жанрам. Добавляем книгу, задаем жанр, проверяем жанр и проверяем что список книг ему соответствует.
    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):

        books_collector.add_new_book('Буратино')
        books_collector.set_book_genre('Буратино', 'Мультфильмы')
        assert books_collector.get_books_with_specific_genre('Мультфильмы') \
               and type(books_collector.get_books_with_specific_genre('Мультфильмы')) == list


11.Тест проверяет что нельзя получить список по определенному жанру, если список пустой или жанр невалидный. Через параметризацию добавляем книги и пробуем получить по жанру список
    @pytest.mark.parametrize('name, genre', [['', 'Фантастика'], ['Чарли Чаплин', 'Комедии']]) 
    def test_get_books_with_specific_genre_empty_list_book_false_genre(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        assert not books_collector.get_books_with_specific_genre('Рассказ')

12. Тест проверяет что нельзя получить пустой список
    def test_get_books_genre_empty_dict(self, books_collector):

        assert not books_collector.get_books_genre()

13. Тест проверяет что в списке с книгами есть только книги с рейтингом для детей. Циклом создаем список и добавляем всем книгам разные жанры. Вторым циклом проверяем есть ли в первом списке жанры 18+
    def test_get_books_for_children_correct_genre(self, books_collector):

       books = ['Лабубу', 'Первое или второе', 'Окончание', 'Василий меняет профессию', 'Ладья']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1

        for rating in books_collector.genre_age_rating:
            assert rating not in books_collector.get_books_for_children()

14. Тест проверяет что книги с рейтингом жанров 18+ не попадают в список книг для детей. Циклом добавляем книги и задаем им жанры 18+, далее ассертим.
    def test_get_books_for_children_adult_rating(self, books_collector):

        books = ['Малышка', 'Гадкий утенок']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre_age_rating[x])
            x += 1

        assert not books_collector.get_books_for_children()

13.Тест проверяет что книга добавленная в избранное есть в избранном. 
def test_add_book_in_favorites_when_books_in_list(self, books_collector):
        books_collector.add_new_book('Гарри Поттер')
        books_collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in books_collector.favorites

14. Тест проверяет что нельзя добавить книгу в избранное, если её нет в списке книг. Циклом добавляем книги в список, затем все их добавляем в избранное, проверяем добавление незнакомой книги.
    def test_add_book_in_favorites_when_book_not_in_list(self, books_collector):

        books = ['Властелин колец', 'Маленький мук', 'Бражник'] #добавляем книги в список и затем в избранное
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert not books_collector.add_book_in_favorites('Мцыри')

15. Тест проверяет удаление книги из избранного. Добавляем книгу в список, затем добавляем ее в избранное и удаляем книгу по названию. В заключении проверяем факт удаления книги из списка избранного
    
       def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book('Знамение')
        books_collector.add_book_in_favorites('Знамение')
        books_collector.delete_book_from_favorites('Знамение')
        assert 'Знамение' not in books_collector.favorites

16. Тест проверяет удаление книги, которой в избранном нет. Добавляем новую книгу в список, затем добавляем ее в избранное. Ассертим попытку удаления несуществующей книги.
       def test_delete_book_from_favorites_no_name_in_list(self, books_collector): 
        books_collector.add_new_book('Муха в шоколаде')
        books_collector.add_book_in_favorites('Муха в шоколаде')
        assert not books_collector.delete_book_from_favorites('Заяц и волк')


17. Тест проверяет метод который возвращает список избранных книг. Циклом добавляем книги в список, затем добавляем всех в избранное. Ассертим получение списка.
    def test_get_list_of_favorites_books_not_empty(self, books_collector):
       books = ['Преступление и наказание', 'Крик', 'Папа купил автомобиль']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)
        assert books_collector.get_list_of_favorites_books()

18.Тест проверяет что после удаления единственной книги из списка избранного, метод получения списка избранного вернет пустой список. Добавляем книгу, зате добавляем её в избранное и удаляем из избранного. Ассертим метод.
        def test_get_list_of_favorites_books_empty_list(self, books_collector):
        books_collector.add_new_book('Бемби')
        books_collector.add_book_in_favorites('Бемби')
        books_collector.delete_book_from_favorites('Бемби')
        assert not books_collector.get_list_of_favorites_books()
import pytest

from app import create_app
from model.book import Book
from model.library import Library

def test_get_booklist(client):
    response = client.get('/booklist')
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert 'A dream of spring' in data

def test_insert_book(client, new_book):
    response = client.post('/book', data=book_asdict(new_book))
    assert response.status_code == 201
    books = Library().book_list
    assert new_book in books

def book_asdict(book):
    return {
        'book_uuid': book.book_uuid,
        'title': book.title,
        'isbn': book.isbn,
        'author': book.author,
        'price': book.price
    }
@pytest.fixture
def new_book():
    return Book(
        book_uuid=None,
        title='The new book',
        isbn='978-0-222-22222-2',
        author='The new guy',
        price=55.65
    )
@pytest.fixture
def library():
    books = Library().book_list
    return books

@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def client(app):
    app.testing = True
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

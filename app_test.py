import shutil

import pytest

from app import create_app
from model.book import Book
from model.library import Library


def test_get_booklist(client):
    response = client.get('/booklist')
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert 'A dream of spring' in data

def test_get_book(client):
    assert True

def test_insert_book(client, new_book):
    response = client.post('/book', data=book_asdict(new_book))
    assert response.status_code == 201
    new_book.book_uuid = response.data.decode('utf-8')

    books = Library().book_list
    assert new_book in books


def test_update_book(client, changed_book):
    response = client.put('/book/c746a291-0ef9-4b2a-8268-392b12d636bd', data=book_asdict(changed_book))
    assert response.status_code == 200

    books = Library().book_list
    assert changed_book in books


def test_delete_book(client):
    response = client.delete('/book/c746a291-0ef9-4b2a-8268-392b12d636bd')
    assert response.status_code == 200
    books = Library().book_list
    assert len(books) == 3


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
def changed_book():
    return Book(
        book_uuid='c746a291-0ef9-4b2a-8268-392b12d636bd',
        title='The book that never was',
        isbn='978-0-333-33333-3',
        author='George my b* Martin',
        price=0.05
    )


@pytest.fixture
def library():
    books = Library().book_list
    return books


@pytest.fixture()
def app():
    app = create_app()
    shutil.copy('./files/books.bak.json', './files/books.json')
    yield app


@pytest.fixture()
def client(app):
    app.testing = True
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

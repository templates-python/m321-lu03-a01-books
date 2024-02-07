from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Book:
    """
    a book in the library
    """
    book_uuid: str
    title: str
    isbn: int
    author: str
    price: float

    @property
    def book_uuid(self):
        return self._book_uuid

    @book_uuid.setter
    def book_uuid(self, value):
        self._book_uuid = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

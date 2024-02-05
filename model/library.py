import json
from dataclasses import dataclass

from model.book import Book


@dataclass
class Library:
    """
    the library containing all the books
    """

    book_list: list[Book]

    def __post_init__(self):
        self._read_books()

    @property
    def book_list(self) -> list:
        return self._book_list

    @book_list.setter
    def book_list(self, value) -> None:
        self._book_list = value


    def save_books(self) -> None:
        """
        converts the book_list into a json-array and writes it to the file
        """
        books_json = '['
        for book in self.book_list:
            books_json += book.to_json() + ','
        books_json = books_json[:-1] + ']'

        with open('./files/books.json', encoding='UTF-8', mode='w') as file:
            file.write(books_json)

    def get_book_by_uuid(self, book_uuid):
        """
        gets a book by its uuid
        """
        for book in self.book_list:
            if book.book_uuid == book_uuid:
                return book
        return None

    def _read_books(self) -> None:
        """
        loads the books from the json file and converts them to a list of Book-objects
        """
        books = list()
        with open('./files/books.json', encoding='UTF-8') as file:
            books_dict = json.load(file)
            for book_json in books_dict:
                book = Book(
                    book_uuid=book_json['book_uuid'],
                    title=book_json['title'],
                    isbn=book_json['isbn'],
                    author=book_json['author'],
                    price=book_json['price'],
                )
                books.append(book)
            pass
        self.book_list = books

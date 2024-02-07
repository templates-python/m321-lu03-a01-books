import uuid

from flask import make_response
from flask_restful import Resource, reqparse

from model.book import Book
from model.library import Library


class BookResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', location='form', default=None, help='book title')
        self.parser.add_argument('isbn', location='form', default=None, help='isbn')
        self.parser.add_argument('author', location='form', default=None, help='author')
        self.parser.add_argument('price', location='form', default=None, help='price')

    def get(self, book_uuid):
        book = Library().get_book_by_uuid(book_uuid)
        if book is None:
            return make_response('[]', 404)
        else:
            return make_response(book.to_json(), 200)

    def put(self, book_uuid):
        """
        update an existing book
        """
        library = Library()
        book = library.get_book_by_uuid(book_uuid)
        if book is None:
            return make_response('', 404)

        args = self.parser.parse_args()
        book.title = args.title
        book.isbn = args.isbn
        book.author = args.author
        book.price = args.price
        library.save_books()
        return make_response('', 200)

    def post(self):
        """
        inserts a new book
        """
        library = Library()
        book = Book()
        args = self.parser.parse_args()
        book.book_uuid = str(uuid.uuid4())
        book.title = args.title
        book.isbn = args.isbn
        book.author = args.author
        book.price = args.price
        library.book_list.append(book)
        library.save_books()
        return make_response('', 200)

    def delete(self, book_uuid):
        """
        deletes a book from the library
        """
        library = Library()
        book = library.get_book_by_uuid(book_uuid)
        if book is None:
            return make_response('', 404)
        position = library.book_list.index(book)
        library.book_list.pop(position)
        library.save_books()
        return make_response('', 200)

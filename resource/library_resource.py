from flask import make_response
from flask_restful import Resource

from model.library import Library


class LibraryResource(Resource):
    def get(self):
        library = Library()
        books = library.book_list
        http_status = 200
        return make_response(
            books, http_status
        )
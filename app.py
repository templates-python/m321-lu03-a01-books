from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resource.book_resource import BookResource
from resource.library_resource import LibraryResource


def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    api.add_resource(LibraryResource, '/booklist')
    api.add_resource(BookResource, '/book/<book_uuid>', '/book')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


from flask import Flask
from flask_restful import Resource, Api

from resource.book_resource import BookResource
from resource.library_resource import LibraryResource

app = Flask(__name__)
api = Api(app)

api.add_resource(LibraryResource, '/booklist')
api.add_resource(BookResource, '/book/<book_uuid>', '/book')

if __name__ == '__main__':
    app.run(debug=True)
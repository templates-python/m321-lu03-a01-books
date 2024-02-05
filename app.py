from flask import Flask
from flask_restful import Api

from resource.book_resource import BookResource
from resource.library_resource import LibraryResource

app = Flask(__name__)
api = Api(app)

# TODO define Resources and paths

if __name__ == '__main__':
    app.run(debug=True)
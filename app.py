from flask import Flask
from flask_restful import Api
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    # TODO define Resources and paths

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


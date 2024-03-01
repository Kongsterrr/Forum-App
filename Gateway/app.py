from flask import Flask
from flask_cors import CORS

from routes.gateway_blueprint import gateway_blueprint


app = Flask(__name__)
app.register_blueprint(gateway_blueprint)

CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == '__main__':
    app.run()

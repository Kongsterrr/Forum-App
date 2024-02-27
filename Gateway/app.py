from flask import Flask

from routes.gateway_blueprint import gateway_blueprint


app = Flask(__name__)
app.register_blueprint(gateway_blueprint)


if __name__ == '__main__':
    app.run()

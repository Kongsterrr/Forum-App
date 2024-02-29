from flask import Flask

from aop.error_handler import initialize_error_handlers
from routes.post_history_blueprint import post_history_blueprint


app = Flask(__name__)
app.register_blueprint(post_history_blueprint)

initialize_error_handlers(app)


if __name__ == '__main__':
    app.run(port=6014)

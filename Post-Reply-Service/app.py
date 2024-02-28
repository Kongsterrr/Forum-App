from flask import Flask

from aop.error_handler import initialize_error_handlers
from routes.post_reply_blueprint import post_reply_blueprint
from models.database import initialize_db


app = Flask(__name__)
app.register_blueprint(post_reply_blueprint)

initialize_error_handlers(app)
initialize_db()


if __name__ == '__main__':
    app.run(port=6006)
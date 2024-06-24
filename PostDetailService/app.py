from flask import Flask
from routes.postDetail_blueprint import postDetail_blueprint
from aop.error_handler import initialize_error_handlers


app = Flask(__name__)
app.register_blueprint(postDetail_blueprint)

initialize_error_handlers(app)



if __name__ == '__main__':
    app.run(port=6080)

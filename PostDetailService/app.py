from flask import Flask
from routes.postDetail_blueprint import postDetail_blueprint

app = Flask(__name__)
app.register_blueprint(postDetail_blueprint)

if __name__ == '__main__':
    app.run()

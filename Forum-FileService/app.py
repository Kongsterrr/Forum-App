from flask import Flask

from routes.file_blueprint import file_blueprint

app = Flask(__name__)
app.register_blueprint(file_blueprint)

if __name__ == '__main__':
    app.run(port=8000,debug=True)

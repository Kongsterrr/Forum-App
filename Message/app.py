from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.message import db
from aop.error_handler import initialize_error_handlers
from routes.message_blueprint import message_blueprint


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:Danmoai0?JWJ@team-blue-database.cbagagysshae.us-east-2.rds.amazonaws.com/Message_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

initialize_error_handlers(app)

db.init_app(app)

with app.app_context():
    # Create database tables
    db.create_all()


app.register_blueprint(message_blueprint)


if __name__ == '__main__':
    app.run()

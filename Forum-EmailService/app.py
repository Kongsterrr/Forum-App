from flask import Flask
import json
from routes.email_blueprint import email_blueprint
from services.email_service import EmailService
import config

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'azure.hrj@gmail.com'  
app.config['MAIL_PASSWORD'] = config.APP_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = 'azure.hrj@gmail.com'  


app.register_blueprint(email_blueprint)

with app.app_context():
    email_service = EmailService(app)

if __name__ == '__main__':
    app.run(port=6012,debug=True)

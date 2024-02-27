import threading
from flask import Flask

from routes.auth_blueprint import auth_blueprint
from services.auth_service import AuthService

app = Flask(__name__)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    # Start the consuming loop in a separate thread
    auth_service = AuthService()
    threading.Thread(target=auth_service.start_listening, daemon=True).start()

    app.run(port=8001, debug=True)

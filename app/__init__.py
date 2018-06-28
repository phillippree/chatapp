from flask import Flask
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
import os

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    Bootstrap(app)
    app.config['SECRET_KEY'] = os.environ.get('CHATAPP_SECRET_KEYS')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app


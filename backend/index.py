"""
Este modulo contiene la inicialización de la aplicación
"""
from flask import Flask
from flask_cors import CORS
from database.db import db
from config import Config
from routes.tasks_routes import tasks_routes


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(tasks_routes)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
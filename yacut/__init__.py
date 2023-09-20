"""
Инициализация и конфигурация приложения.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings import Config
from yacut.config import configure_logging

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
configure_logging()

from yacut import views, api_views, error_handlers

if __name__ == '__main__':
    app.run()

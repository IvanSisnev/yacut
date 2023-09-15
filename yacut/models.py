"""
Модели проекта.
"""

from datetime import datetime

from yacut import db


class URLMap(db.Model):
    """Модель БД проекта: таблица url адресов."""
    id = db.Column(db.Integer, primary_key=True)
    # поле оригинальной ссылки
    original = db.Column(db.String(), nullable=False)
    # поле короткого alias
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

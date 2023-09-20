"""
Модели приложения.
"""
from datetime import datetime

from yacut import db
from settings import ORIGINAL_MAX_LENGTH, SHORT_MAX_LENGTH


class URLMap(db.Model):
    """
    Модель БД проекта: таблица url адресов.
    """
    id = db.Column(db.Integer, primary_key=True)
    # поле оригинальной (длинной) ссылки
    original = db.Column(db.String(ORIGINAL_MAX_LENGTH), nullable=False)
    # поле короткой ссылки (псевдонима)
    short = db.Column(db.String(SHORT_MAX_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return {
            'url': self.original,
            'custom_id': self.short,
        }

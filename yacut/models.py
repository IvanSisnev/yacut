"""
Модели приложения.
"""
from datetime import datetime

from flask import url_for

from yacut import db
from settings import ORIGINAL_MAX_LENGTH, SHORT_MAX_LENGTH


class URLMap(db.Model):
    """
    Модель БД проекта: таблица url адресов и их псевдонимов.
    """
    id = db.Column(db.Integer, primary_key=True)
    # поле оригинальной (длинной) ссылки
    original = db.Column(db.String(ORIGINAL_MAX_LENGTH), nullable=False)
    # поле короткой ссылки (псевдонима)
    short = db.Column(db.String(SHORT_MAX_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def original_short_serializer(self, mode=None):
        """
        Сериализует поля original и short для передачи на эндпоинты.
        """
        if mode == 'original_only':
            return {'url': self.original}
        return {
            'short_link': (url_for('index_page', _external=True) + self.short),
            'url': self.original
        }

"""
Установки и константы приложения.
"""
import os
from string import ascii_letters, digits
from typing import Final


class Config(object):
    """Конфиг."""
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        default='sqlite:///db.sqlite3'
    )
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        default='BoIgdhnwlsRMaWF'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# набор символов для генерации короткой ссылки (псевдонима)
CUSTOM_ID_SEQUENCE: Final[list] = list(ascii_letters + digits)

# длина генерируемой короткой ссылки
CUSTOM_ID_LENGTH: Final[int] = 6

# максимальная длина оригинального url адреса
ORIGINAL_MAX_LENGTH: Final[int] = 256

# допустимая длина короткой ссылки, переданной пользователем
SHORT_MIN_LENGTH: Final[int] = 1
SHORT_MAX_LENGTH: Final[int] = 16

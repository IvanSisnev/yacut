"""
Установки и константы приложения.
"""
import os
from string import ascii_letters, digits
from typing import Final


class Config(object):
    """Конфиг."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


# набор символов для генерации короткой ссылки (псевдонима)
CUSTOM_ID_SEQUENCE: Final[list] = list(ascii_letters + digits)

# длина короткой ссылки
CUSTOM_ID_LENGTH: Final[int] = 6

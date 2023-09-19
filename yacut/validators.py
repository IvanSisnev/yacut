"""
Валидаторы приложения.
"""
from settings import CUSTOM_ID_SEQUENCE
from yacut.models import URLMap


def check_for_unallowed_chars(short_id: str) -> bool:
    """
    Проверяет на недопустимые символы короткую ссылку, переданную
    пользователем.
    :param short_id: строка со ссылкой.
    :return: True если недопустимые символы не обнаружены.
    """
    return all(char in CUSTOM_ID_SEQUENCE for char in short_id)


def check_for_duplicates(short_id: str) -> bool:
    """
    Проверяет на уникальность короткую ссылку, переданную пользователем.
    :param short_id: строка со ссылкой.
    :return: True если ссылка уникальна.
    """
    return URLMap.query.filter_by(short=short_id).first() is None

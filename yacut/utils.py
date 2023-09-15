"""
Утилиты приложения.
"""
from random import choices

from settings import CUSTOM_ID_SEQUENCE, CUSTOM_ID_LENGTH
from yacut.models import URLMap


def get_unique_short_id() -> str:
    """
    Создает строку заданной длины из символов, выбранных случайным
    образом из заданной последовательности. Проверяет ее на уникальность.
    :return: строка
    """
    short_id: str = ''.join(choices(CUSTOM_ID_SEQUENCE, k=CUSTOM_ID_LENGTH))
    # если такая же строка уже есть в БД
    if not check_for_duplicates(short_id):
        get_unique_short_id()
    return short_id


def check_for_duplicates(short_id: str) -> bool:
    """
    Проверяет короткую ссылку на уникальность в БД.
    :return: True ссылка уникальна.
    """
    return URLMap.query.filter_by(short=short_id).first() is None

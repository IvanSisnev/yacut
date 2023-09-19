"""
Утилиты приложения.
"""
from random import choices

from settings import CUSTOM_ID_SEQUENCE, CUSTOM_ID_LENGTH
from yacut.validators import check_for_duplicates


def get_unique_short_id() -> str:
    """
    Создает строку заданной длины из символов, выбранных случайным
    образом из заданной последовательности.
    Проверяет ее на уникальность в БД.
    :return: строка
    """
    short_id: str = ''.join(choices(CUSTOM_ID_SEQUENCE,
                                    k=CUSTOM_ID_LENGTH))
    # если такая строка уже есть в БД
    if not check_for_duplicates(short_id):
        get_unique_short_id()
    return short_id

"""
Утилиты приложения.
"""
from random import choices

from settings import CUSTOM_ID_SEQUENCE, CUSTOM_ID_LENGTH


def get_unique_short_id() -> str:
    """
    Создает строку заданной длины из символов, выбранных случайным
    образом из заданной последовательности.
    :return: строка
    """
    return ''.join(choices(CUSTOM_ID_SEQUENCE, k=CUSTOM_ID_LENGTH))

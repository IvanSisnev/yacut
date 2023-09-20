"""
Конфиг приложения.
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from settings import BASE_DIR, DT_FORMAT, LOG_FORMAT


def configure_logging():
    """
    Конфигурирует логирование.
    """
    # создаю директорию для логов
    log_dir: Path = Path.joinpath(BASE_DIR, 'logs')
    Path(log_dir).mkdir(exist_ok=True)
    # создаю путь для сохранения файла в директорию
    log_file: Path = Path.joinpath(log_dir, 'yacut_log.log')

    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10 ** 6, backupCount=5
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )

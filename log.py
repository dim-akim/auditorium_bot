"""
Модуль содержит функцию get_logger с настройками для общего логгера:
    Уровень логгера - logging.INFO
    Количество обработчиков - 2:
        console_handler - вывод в консоль (уровень DEBUG)
        file_handler - вывод в файл с именем LOG_FILE (уровень INFO)

    Файлы будут расположены в папке ../LOG_FOLDER/, которая создается в процессе импорта или запуска модуля

Используется библиотека logging
"""

import logging
from logging.handlers import TimedRotatingFileHandler
import sys
from pathlib import Path


LOG_FOLDER = Path.cwd() / 'logs'  # имя папки с логами
LOG_FOLDER.mkdir(exist_ok=True)  # создаем папку для логов. exist_ok - если папка уже есть, не будет ошибки

LOG_FILE = 'log_service_bot.log'  # имя для общего лог-файла

# формат для одного лог-сообщения. Параметры:
#   %(asctime)s - время в формате гггг-мм-дд чч:мм:сс,мс
#   %(levelname)s - уровень сообщения (INFO, WARNING и т.п.)
#   %(name)s - имя логгера
#   %(filename)s - имя файла
#   %(module)s - имя модуля
#   %(funcName)s - имя функции
#   %(lineno)d - номер строчки
#   %(message)s - текст лог-сообщения
FORMATTER = logging.Formatter(
    f'%(asctime)s  [%(levelname)s] | (%(module)s) | %(message)s'
)


def get_logger(name: str) -> logging.Logger:
    """
    Возвращает логгер с тремя обработчиками сообщений:
        console_handler - вывод в консоль (уровень DEBUG)
        file_handler - вывод в файл с именем LOG_FILE (уровень INFO)
    Файлы будут расположены в папке ../LOG_FOLDER/
    """

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(logging.DEBUG)

    file_handler = TimedRotatingFileHandler(LOG_FOLDER / LOG_FILE, 'W0')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.INFO)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

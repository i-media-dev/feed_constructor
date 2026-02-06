import os

from dotenv import load_dotenv

load_dotenv()

DATE_FORMAT = '%Y-%m-%d'
"""Формат даты по умолчанию."""

TIME_FORMAT = '%H:%M:%S'
"""Формат времени по умолчанию."""

ATTEMPTION_LOAD_FEED = 3
"""Попытки для скачивания фида."""

FEEDS_FOLDER = os.getenv('FEEDS_FOLDER', 'input_feeds')
"""Папка с фидами по умолчанию."""

OBJECTS = {
    'cian': 'object',
    'avito': 'Ad',
    'yandex': 'offer',
}
"""Словарь соответствия тега объекта и площадки."""

IDS_CIAN = 'https://www.cian.ru/newObjects/feed/'
"""Ссылка на фид xml с id жк CIAN."""

IDS_YANDEX = 'https://realty.yandex.ru/newbuildings.tsv'
"""Ссылка на файл tsv с id жк YANDEX."""

IDS_AVITO = 'https://autoload.avito.ru/format/New_developments.xml'
"""Ссылка на фид xml с id жк AVITO."""

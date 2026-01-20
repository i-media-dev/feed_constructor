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

import json
import logging
import os
from datetime import datetime as dt
from pathlib import Path

from constructor.constants.constants import DATE_FORMAT
from constructor.exceptions import DirectoryCreationError, EmptyFeedsListError
from constructor.settings.logging_config import setup_logging

setup_logging()


def get_filenames_list(folder_name: str) -> list[str]:
    """Функция, возвращает список названий фидов."""
    folder_path = Path(__file__).parent.parent / folder_name
    if not folder_path.exists():
        logging.error('Папка %s не существует', folder_name)
        raise DirectoryCreationError('Папка %s не найдена', folder_name)
    files_names = [
        file.name for file in folder_path.iterdir() if file.is_file()
    ]
    if not files_names:
        logging.error('В папке нет файлов')
        raise EmptyFeedsListError('Нет скачанных файлов')
    logging.debug('Найдены файлы: %s', files_names)
    return files_names


def save_to_json(
    data: dict,
    prefix: str,
    folder: str = 'test_data'
) -> None:
    """Отладочный метод сохраняет данные в файл формата json."""
    os.makedirs(folder, exist_ok=True)
    date_str = (dt.now()).strftime(DATE_FORMAT)
    filename = os.path.join(folder, f'{prefix}_{date_str}.json')
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logging.info(f'✅ Данные сохранены в {filename}')
    logging.debug('Файл сохранен.')

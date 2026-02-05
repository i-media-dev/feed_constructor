import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from constructor.mixins import FileMixin


class FeedCreator(ABC, FileMixin):

    def __init__(self, filename: str, foldername: str, data: list):
        self.filename = filename
        self.foldername = foldername
        self.data = data

    @abstractmethod
    def build_feed(self) -> ET.Element:
        pass

    def _append_dict(self, parent: ET.Element, data: dict):
        for key, value in data.items():
            self._append_value(parent, key, value)

    def _append_value(self, parent: ET.Element, key: str, value: Any):
        if value is None:
            return

        if isinstance(value, (str, int, float)):
            element = ET.SubElement(parent, key)
            element.text = str(value)

        elif isinstance(value, dict):
            element = ET.SubElement(parent, key)
            self._append_dict(element, value)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    element = ET.SubElement(parent, key)
                    self._append_dict(element, item)
                else:
                    element = ET.SubElement(parent, key)
                    element.text = str(item)

        else:
            raise TypeError(
                f'Неподдерживаемый тип для ключа "{key}": {type(value)}'
            )

    def create_and_save_feed(self) -> Path:
        root = self.build_feed()
        self._indent(root)

        tree = ET.ElementTree(root)
        folder_path = self._make_dir(self.foldername)
        file_path = folder_path / self.filename
        tree.write(
            file_path,
            encoding='utf-8',
            xml_declaration=True
        )
        return file_path


class AvitoFeedCreator(FeedCreator):

    def build_feed(self) -> ET.Element:
        root = ET.Element(
            'Ads',
            {'formatVersion': '3', 'target': 'Avito.ru'}
        )
        for object in self.data:
            ad = ET.SubElement(root, 'Ad')
            self._append_dict(ad, object)

        return root


class CianFeedCreator(FeedCreator):

    def build_feed(self) -> ET.Element:
        root = ET.Element('feed')
        feed_version = ET.SubElement(root, 'feed_version')
        feed_version.text = "2"

        for object in self.data:
            obj = ET.SubElement(root, 'object')
            self._append_dict(obj, object)

        return root


class YandexFeedCreator(FeedCreator):

    def build_feed(self) -> ET.Element:
        root = ET.Element(
            'realty-feed',
            {'xmlns': 'http://webmaster.yandex.ru/schemas/feed/realty/2010-06'}
        )
        dt = datetime.now(timezone(timedelta(hours=4)))
        generation_date = ET.SubElement(root, 'generation-date')
        generation_date.text = str(dt)
        for object in self.data:
            offer = ET.SubElement(
                root,
                'offer',
                {'internal-id': object['internal-id']}
            )
            self._append_dict(offer, object)

        return root

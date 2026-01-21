import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

from constructor.mixins import FileMixin


class YandexFeedCreator(FileMixin):

    def __init__(self, data: list[dict]):
        self.data = data

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

    def _append_dict(self, parent: ET.Element, data: dict):
        for key, value in data.items():
            self._append_value(parent, key, value)

    def _append_value(self, parent: ET.Element, key: str, value):
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

    def create_and_save_feed(self, filename='yandex_test.xml'):
        root = self.build_feed()
        self._indent(root)

        tree = ET.ElementTree(root)
        folder_path = self._make_dir('yandex_feeds')
        file_path = folder_path / filename
        tree.write(
            file_path,
            encoding='utf-8',
            xml_declaration=True
        )
        return file_path

import xml.etree.ElementTree as ET
from abc import abstractmethod

from constructor.mixins import FileMixin


class FeedCreator(FileMixin):

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

    def create_and_save_feed(self):
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

import xml.etree.ElementTree as ET

from constructor.mixins import FileMixin
from constructor.avito_constants import SIMPLE_FIELDS, LIST_FIELDS


class AvitoFeedCreator(FileMixin):

    def __init__(self, data: dict):
        self.data = data

    def _append_value(self, parent, key, value):
        if value is None:
            return

        if isinstance(value, dict):
            element = ET.SubElement(parent, key)
            for k, v in value.items():
                self._append_value(element, k, v)

        elif isinstance(value, list):
            self._append_list(parent, key, value)

        else:
            element = ET.SubElement(parent, key)
            element.text = str(value)

    def _append_list(self, parent, key, items):
        wrapper = ET.SubElement(parent, key)

        for item in items:
            item_element = ET.SubElement(wrapper, item)
            if isinstance(item, dict):
                for k, v in item.items():
                    self._append_value(item_element, k, v)
            else:
                item_element.text = str(item)

    def build_feed(self):
        root = ET.Element('Ads')
        root.set('formatVersion', '3')
        root.set('target', 'Avito.ru')

        object_element = ET.SubElement(root, 'Ad')

        for key in SIMPLE_FIELDS:
            value = self.data.get(key)
            if value is not None:
                element = ET.SubElement(object_element, key)
                element.text = str(value)

        for key in LIST_FIELDS:
            items = self.data.get(key, [])
            if items:
                self._append_list(object_element, key, items)

        return root

    def create_and_save_feed(self, filename='avito_test.xml'):
        root = self.build_feed()
        self._indent(root)

        tree = ET.ElementTree(root)
        folder_path = self._make_dir('avito_feeds')
        file_path = folder_path / filename
        tree.write(
            file_path,
            encoding='utf-8',
            xml_declaration=True
        )
        return file_path

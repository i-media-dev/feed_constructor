import logging

from constructor.mixins import FileMixin
from constructor.settings.logging_config import setup_logging

setup_logging()


class FeedParser(FileMixin):

    def __init__(
        self,
        filename: str,
        feeds_folder: str,
        fields: dict,
        path_tag: str
    ):
        self.filename = filename
        self.feeds_folder = feeds_folder
        self.fields = fields
        self.path_tag = path_tag
        self._root = None

    @property
    def root(self):
        """Ленивая загрузка корневого элемента."""
        if self._root is None:
            self._root = self._get_root(self.filename, self.feeds_folder)
            logging.info('Корневой элемент - %s', self.root)
        return self._root

    def _parse_field(self, node, config: dict):
        field_type = config['type']

        if field_type == 'text':
            el = node.find(config['path'])
            return el.text.strip() if el is not None and el.text else None

        if field_type == 'object':
            parent = node.find(config['path'])
            if parent is None:
                return None

            result = {}
            for name, sub in config['fields'].items():
                if isinstance(sub, dict):
                    result[name] = self._parse_field(parent, sub)
                else:
                    el = parent.find(sub)
                    result[name] = el.text.strip(
                    ) if el is not None and el.text else None
            return result

        if field_type == 'list':
            result = []
            for item_node in node.findall(config['path']):
                item = {}
                for name, sub in config['fields'].items():
                    if isinstance(sub, dict) and 'attr' in sub:
                        item[name] = item_node.attrib.get(sub['attr'])
                    else:
                        el = item_node.find(sub)
                        item[name] = el.text.strip(
                        ) if el is not None and el.text else None
                result.append(item)
            return result

    def _parse_object(self, node) -> dict:
        data: dict = {}

        for field_name, field_config in self.fields.items():
            value = self._parse_field(node, field_config)
            if value is not None:
                data[field_name] = value

        return data

    def parse_objects(self) -> list[dict]:
        data = []
        objects = self.root.findall(f'.//{self.path_tag}')

        logging.info('Найдено %s объектов', len(objects))

        for obj in objects:
            offer = self._parse_object(obj)
            data.append(offer)

        return data

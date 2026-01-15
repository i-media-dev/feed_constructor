import xml.etree.ElementTree as ET

from constructor.mixins import FileMixin


class CianFeedCreator(FileMixin):

    def __init__(self, data: dict):
        self.data = data

    def build_feed(self):
        root = ET.Element('feed')
        feed_version = ET.Element('feed_version')
        feed_version.text = "2"
        root.append(feed_version)

        object = ET.Element('object')
        root.append(object)

        category = ET.Element('Category')
        category.text = self.data.get('Category')
        object.append(category)
        return root

    def save(self):
        root = self.build_feed()
        self._indent(root)

        tree = ET.ElementTree(root)

        folder_path = self._make_dir('cian_feeds')
        file_path = folder_path / 'cian_test.xml'
        tree.write(
            file_path,
            encoding='utf-8',
            xml_declaration=True
        )

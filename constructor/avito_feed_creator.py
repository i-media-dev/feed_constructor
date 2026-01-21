import xml.etree.ElementTree as ET

from constructor.feed_creator import FeedCreator


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

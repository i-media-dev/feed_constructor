import xml.etree.ElementTree as ET

from constructor.feed_creator import FeedCreator


class CianFeedCreator(FeedCreator):

    def build_feed(self) -> ET.Element:
        root = ET.Element('feed')
        feed_version = ET.SubElement(root, 'feed_version')
        feed_version.text = "2"

        for object in self.data:
            ad = ET.SubElement(root, 'Ad')
            self._append_dict(ad, object)

        return root

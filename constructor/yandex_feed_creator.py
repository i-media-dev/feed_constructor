import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

from constructor.feed_creator import FeedCreator


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

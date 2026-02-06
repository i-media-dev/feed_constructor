import json
import logging
from pprint import pprint

from constructor.constants.avito_constants import AVITO_FIELDS
from constructor.constants.cian_constants import CIAN_FIELDS
from constructor.constants.constants import FEEDS_FOLDER, OBJECTS
from constructor.constants.yandex_constants import YANDEX_FIELDS
from constructor.constructors.avito_constructor import AvitoNewFlatConstructor
from constructor.constructors.cian_constructor import CianNewFlatConstructor
from constructor.constructors.yandex_constructor import \
    YandexNewFlatConstructor
from constructor.decorators import time_of_script
from constructor.feed_creator import (AvitoFeedCreator, CianFeedCreator,
                                      YandexFeedCreator)
from constructor.feeds_save import FeedSaver
from constructor.parsers.feed_parser import FeedParser
from constructor.settings.logging_config import setup_logging
from constructor.utils import get_filenames_list, save_to_json

setup_logging()


@time_of_script
def main():
    try:
        # feed_saver = FeedSaver()
        # feed_saver.save_xml()

        # filenames = get_filenames_list(FEEDS_FOLDER)
        parser = FeedParser(
            'developer_cian22.xml',
            FEEDS_FOLDER,
            CIAN_FIELDS,
            OBJECTS['cian']
        )
        data_cian = parser.parse_objects()
        save_to_json(data_cian[0], 'cian')

        parser = FeedParser(
            'developer_avito22.xml',
            FEEDS_FOLDER,
            AVITO_FIELDS,
            OBJECTS['avito']
        )
        data_avito = parser.parse_objects()
        save_to_json(data_avito[0], 'avito')

        # parser = FeedParser(
        #     'developer_yandex22.xml',
        #     FEEDS_FOLDER,
        #     YANDEX_FIELDS,
        #     OBJECTS['yandex']
        # )
        # data_yandex = parser.parse_objects()
        # json.dumps(data_yandex[0], ensure_ascii=False, indent=2)
        # pprint(data_yandex[0])

        # for filename in filenames:
        #     parser = FeedParser(filename, FEEDS_FOLDER, CIAN_FIELDS, OBJECTS['cian'])
        #     assembler = ....
        #
        #     cian_constructor = CianNewFlatConstructor()
        #     avito_constructor = AvitoNewFlatConstructor()
        #     yandex_constructor = YandexNewFlatConstructor()

        #     cian_feed_creator = CianFeedCreator(
        #         'cian_feed.xml',
        #         'cian_feeds',
        #         objects
        #     )
        #     yandex_feed_creator = YandexFeedCreator(
        #         'yandex_feed.xml',
        #         'yandex_feeds',
        #         objects
        #     )
        #     avito_feed_creator = AvitoFeedCreator(
        #         'avito_feed.xml',
        #         'avito_feeds',
        #         objects
        #     )

        #     cian_feed_creator.create_and_save_feed()
        #     yandex_feed_creator.create_and_save_feed()
        #     avito_feed_creator.create_and_save_feed()
    except Exception as error:
        logging.error('Ошибка: %s', error)
        raise


if __name__ == '__main__':
    main()

import logging

from constructor.constants.avito_constants import TEST_AVITO_DICT
from constructor.constants.cian_constants import CIAN_FIELDS
from constructor.constants.constants import FEEDS_FOLDER
from constructor.constants.yandex_constants import TEST_YANDEX_DICT
from constructor.constructors.avito_constructor import AvitoNewFlatConstructor
from constructor.constructors.cian_constructor import CianNewFlatConstructor
from constructor.constructors.yandex_constructor import \
    YandexNewFlatConstructor
from constructor.decorators import time_of_script
from constructor.feed_creator import (AvitoFeedCreator, CianFeedCreator,
                                      YandexFeedCreator)
from constructor.feeds_save import FeedSaver
from constructor.logging_config import setup_logging
from constructor.parsers.feed_parser import FeedParser
from constructor.utils import get_filenames_list

from pprint import pprint

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
        )
        data = parser.parse_objects()
        pprint(data)

        # for filename in filenames:
        #     parser = FeedParser(filename, FEEDS_FOLDER, CIAN_DICT)
        #     cian_constructor = CianNewFlatConstructor()
        #     avito_constructor = AvitoNewFlatConstructor()
        #     yandex_constructor = YandexNewFlatConstructor()

        #     cian_feed_creator = CianFeedCreator(
        #         'cian_feed.xml',
        #         'cian_feeds',
        #         [TEST_CIAN_DICT,]
        #     )
        #     yandex_feed_creator = YandexFeedCreator(
        #         'yandex_feed.xml',
        #         'yandex_feeds',
        #         [TEST_YANDEX_DICT,]
        #     )
        #     avito_feed_creator = AvitoFeedCreator(
        #         'avito_feed.xml',
        #         'avito_feeds',
        #         [TEST_AVITO_DICT,]
        #     )

        #     cian_feed_creator.create_and_save_feed()
        #     yandex_feed_creator.create_and_save_feed()
        #     avito_feed_creator.create_and_save_feed()
    except Exception as error:
        logging.error('Ошибка: %s', error)
        raise


if __name__ == '__main__':
    main()

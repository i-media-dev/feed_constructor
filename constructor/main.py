import logging

from constructor.avito_constants import TEST_AVITO_DICT
from constructor.avito_constructor import AvitoDictConstructor
from constructor.cian_constants import TEST_CIAN_DICT
from constructor.cian_constructor import CianDictConstructor
from constructor.decorators import time_of_script
from constructor.feed_creator import (AvitoFeedCreator, CianFeedCreator,
                                      YandexFeedCreator)
from constructor.feeds_save import FeedSaver
from constructor.logging_config import setup_logging
from constructor.yandex_constants import TEST_YANDEX_DICT
from constructor.yandex_constructor import YandexDictConstructor

setup_logging()


@time_of_script
def main():
    try:
        feed_saver = FeedSaver()
        cian_feed_creator = CianFeedCreator(
            'cian_feed.xml',
            'cian_feeds',
            [TEST_CIAN_DICT,]
        )
        yandex_feed_creator = YandexFeedCreator(
            'yandex_feed.xml',
            'yandex_feeds',
            [TEST_YANDEX_DICT,]
        )
        avito_feed_creator = AvitoFeedCreator(
            'avito_feed.xml',
            'avito_feeds',
            [TEST_AVITO_DICT,]
        )
        feed_saver.save_xml()
        cian_feed_creator.create_and_save_feed()
        yandex_feed_creator.create_and_save_feed()
        avito_feed_creator.create_and_save_feed()
    except Exception as error:
        logging.error('Ошибка: %s', error)
        raise


if __name__ == '__main__':
    main()

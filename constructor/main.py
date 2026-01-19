import logging

from constructor.avito_feed_creator import AvitoFeedCreator
from constructor.cian_constants import TEST_CIAN_DICT
from constructor.cian_constructor import CianDictConstructor
from constructor.cian_feed_creator import CianFeedCreator
from constructor.decorators import time_of_script
from constructor.logging_config import setup_logging
from constructor.yandex_constants import TEST_YANDEX_DICT
from constructor.yandex_feed_creator import YandexFeedCreator

# from constructor.avito_constants import

setup_logging()


# @time_of_script
def main():
    try:
        cian_feed_creator = CianFeedCreator(TEST_CIAN_DICT)
        yandex_feed_creator = YandexFeedCreator(TEST_YANDEX_DICT)
        # avito_feed_creator = AvitoFeedCreator()
        cian_feed_creator.create_and_save_feed()
        yandex_feed_creator.create_and_save_feed()
    except Exception as error:
        print(f'Неожиданная ошибка: {error}')
        raise


if __name__ == '__main__':
    main()

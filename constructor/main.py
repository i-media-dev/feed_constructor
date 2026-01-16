import logging

from constructor.cian_constructor import CianDictConstructor
from constructor.cian_feed_creator import CianFeedCreator
from constructor.decorators import time_of_script
from constructor.logging_config import setup_logging

setup_logging()

test_dict = {
    'Category': 'flatRent',
    'Address': 'Москва, Севастопольский пр-т, дом 16',
    'Phones': [
        {
            'CountryCode': '+7',
            'Number': '9156033754'
        },
        {
            'CountryCode': '+7',
            'Number': '9105630748'
        }
    ]
}


@time_of_script
def main():
    cian_feed_creator = CianFeedCreator(test_dict)
    cian_feed_creator.create_and_save_feed()


if __name__ == '__main__':
    main()

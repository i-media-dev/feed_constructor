import logging

# from constructor.decorators import time_of_script
from constructor.logging_config import setup_logging
from constructor.cian_constructor import CianFeedConstructor
from constructor.cian_feed_creator import CianFeedCreator

setup_logging()


# @time_of_script
def main():
    cian_feed_creator = CianFeedCreator({'Category': 'flatRent'})
    cian_feed_creator.build_feed
    cian_feed_creator.save()


if __name__ == '__main__':
    main()

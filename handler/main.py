import logging

from handler.decorators import time_of_script
from handler.logging_config import setup_logging

setup_logging()


@time_of_script
def main():
    pass


if __name__ == '__main__':
    main()

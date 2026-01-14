import logging

from constructor.decorators import time_of_script
from constructor.logging_config import setup_logging

setup_logging()


@time_of_script
def main():
    pass


if __name__ == '__main__':
    main()

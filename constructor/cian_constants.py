import os

from dotenv import load_dotenv

load_dotenv()

SIMPLE_FIELDS = (
    'Category',
    'ExternalId',
    'Description',
    'Address',
    'FlatRoomsCount',
    'TotalArea'
)
"""Простые поля без вложенности."""

FIELDS_WITH_SCHEMA = (
    'Phones',
    'Photos',
    'Videos',
    'Undergrounds'
)
"""Поля с вложенностью schema."""

SCHEMA_NAMES = {
    'Phones': 'PhoneSchema',
    'Photos': 'PhotoSchema',
    'Videos': 'VideoSchema',
    'Undergrounds': 'UndergroundInfoSchema'
}
"""Поля и название схемы, которое к ним относится."""

TEST_CIAN_DICT = {
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

import os

from dotenv import load_dotenv

load_dotenv()

SIMPLE_FIELDS = (
    'Category',
    'ExternalId',
    'Description',
    'Address',
    'FlatRoomsCount',
    'TotalArea',
    'FloorNumber',
    'Email'
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
    'ExternalId': '1241512',
    'Description': 'owfjkpoqkro qqwjfr pqowfq jqpowrfjk poqakfp qpjwef qpwe',
    'Address': 'Москва, Севастопольский пр-т, дом 16',
    'FlatRoomsCount': '2',
    'Phones': [
        {
            'CountryCode': '+7',
            'Number': '9156033754'
        },
        {
            'CountryCode': '+7',
            'Number': '9105630748'
        }
    ],
    'TotalArea': '60',
    'FloorNumber': '5',
    'Email': 'wwdawdada@mail.ru'

}

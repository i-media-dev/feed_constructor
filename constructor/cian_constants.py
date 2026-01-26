import os

from dotenv import load_dotenv

load_dotenv()

IDS_CIAN = ''
"""Ссылка на фид с id жк CIAN."""

REQUIRED_CIAN_FIELDS_FOR_FLAT_SALE = [
    'Category',
    'ExternalId',
    'Description',
    'Address',
    'FlatRoomsCount',
    'TotalArea',
    'Phones',
    'Email',
]
"""Множество обязательных полей для продажи квартиры для CIAN."""


TEST_CIAN_DICT = {
    'Category': 'flatRent',
    'ExternalId': '1241512',
    'Description': 'owfjkpoqkro qqwjfr pqowfq jqpowrfjk poqakfp qpjwef qpwe',
    'Address': 'Москва, Севастопольский пр-т, дом 16',
    'FlatRoomsCount': '2',
    'Phones': {
        'PhoneSchema': [
            {'CountryCode': '+7', 'Number': '9156033754'},
            {'CountryCode': '+7', 'Number': '9105630748'}
        ]
    },
    'TotalArea': '60',
    'FloorNumber': '5',
    'Email': 'wwdawdada@mail.ru',
    'BargainTerms': {
        'Price': '10 000 000',
        'SaleType': 'Свободная продажа',
        'AgentBonus': {
            'Value': '20'
        },
    },
    'JKSchema': {
        'Id': '131',
        'Name': 'Метропарк',
        'House':
            {
                'Id': '13141',
            }
    },

}

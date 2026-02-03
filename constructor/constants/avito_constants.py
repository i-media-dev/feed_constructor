import os

from dotenv import load_dotenv

load_dotenv()


AVITO_FIELDS = {
    'id': {
        'path': 'Id',
        'type': 'text',
    },
    'description': {
        'path': 'Description',
        'type': 'text',
    },
    'category': {
        'path': 'Category',
        'type': 'text',
    },
    'operation_type': {
        'path': 'OperationType',
        'type': 'text',
    },
    'price': {
        'path': 'Price',
        'type': 'text',
    },
    'market_type': {
        'path': 'MarketType',
        'type': 'text',
    },
    'house_type': {
        'path': 'HouseType',
        'type': 'text',
    },
    'floor': {
        'path': 'Floor',
        'type': 'text',
    },
    'floors': {
        'path': 'Floors',
        'type': 'text',
    },
    'rooms': {
        'path': 'Rooms',
        'type': 'text',
    },
    'square': {
        'path': 'Square',
        'type': 'text',
    },
    'status': {
        'path': 'Status',
        'type': 'text',
    },
    'development_id': {
        'path': 'NewDevelopmentId',
        'type': 'text',
    },
    'property_rights': {
        'path': 'PropertyRights',
        'type': 'text',
    },
    'decoration': {
        'path': 'Decoration',
        'type': 'text',
    },
    'images': {
        'path': 'Images',
        'type': 'list',
        'fields': {
            'url': {
                'attr': 'url'
            }
        }
    }
}
"""Обязательные поля для парсинга фида AVITO."""

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

CIAN_FIELDS = {
    'category': {
        'path': 'ExternalId',
        'type': 'text',
    },
    'id': {
        'path': 'Category',
        'type': 'text',
    },
    'description': {
        'path': 'Description',
        'type': 'text',
    },
    'address': {
        'path': 'Address',
        'type': 'text'
    },
    'rooms': {
        'path': 'FlatRoomsCount',
        'type': 'text',
    },
    'phones': {
        'path': 'Phones/PhoneSchema',
        'type': 'list',
        'fields': {
            'country_code': 'CountryCode',
            'number': 'Number',
        }
    },
    'area': {
        'path': 'TotalArea',
        'type': 'text',
    },
    'floor': {
        'path': 'FloorNumber',
        'type': 'text',
    },
    'jk': {
        'path': 'JKSchema',
        'type': 'text',
    },
    'email': {
        'path': 'Email',
        'type': 'text',
    },
    'photos': {
        'path': 'Photos/PhotoSchema',
        'type': 'list',
        'fields': {
            'url': 'FullUrl',
            'is_default': 'IsDefault',
        }
    },
    'building': {
        'path': 'Building',
        'type': 'object',
        'fields': {
            'floors': 'FloorsCount',
        }
    },
    'cpl_moderation': {
        'path': 'CplModeration',
        'type': 'object',
        'fields': {
            'person_type': 'PersonType',
        }
    },
    'bargain_terms': {
        'path': 'BargainTerms',
        'type': 'object',
        'fields': {
            'price': 'Price',
            'sale_type': 'SaleType',
            'agent_bonus': {
                'type': 'object',
                'path': 'AgentBonus',
                'fields': {
                    'value': 'Value'
                }
            }
        }
    }
}

import os

from dotenv import load_dotenv

from constructor.models.model_seller import SellerCategory
from constructor.models.model_new_flat import Currency

load_dotenv()


CIAN_SELLER_MAP = {
    # 'юридическое лицо': SellerCategory.COMPANY,
    # 'частное лицо': SellerCategory.OWNER,
    'legal': SellerCategory.COMPANY,
    'natural': SellerCategory.OWNER,
}
"""Маппер продажника для CIAN."""

CIAN_CURRENCY_MAP = {
    'eur': Currency.EUR,
    'rur': Currency.RUB,
    'usd': Currency.USD
}
"""Маппер валюты для CIAN."""

CIAN_FIELDS = {
    'category': {
        'path': 'Category',
        'type': 'text',
    },
    'id': {
        'path': 'ExternalId',
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
        'type': 'object',
        'fields': {
            'id': 'Id',
            'name': 'Name',
            'house': {
                'type': 'object',
                'path': 'House',
                'fields': {
                    'id': 'Id',
                    'name': 'Name'
                }
            }
        }
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
            'currency': 'Currency',
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
"""Обязательные поля для парсинга фида CIAN."""

import os

from dotenv import load_dotenv

load_dotenv()


YANDEX_FIELDS = {
    'type': {
        'path': 'type',
        'type': 'text',
    },
    'property_type': {
        'path': 'property-type',
        'type': 'text',
    },
    'category': {
        'path': 'category',
        'type': 'text',
    },
    'creation_date': {
        'path': 'creation-date',
        'type': 'text',
    },
    'deal_status': {
        'path': 'deal-status',
        'type': 'text',
    },
    'location': {
        'path': 'location',
        'type': 'object',
        'fields': {
            'country': 'country',
            'locality': 'locality-name',
            'address': 'address',
            'metro': {
                'type': 'object',
                'path': 'metro',
                'fields': {
                    'name': 'name',
                }
            }
        }
    },
    'price': {
        'path': 'price',
        'type': 'object',
        'fields': {
            'value': 'value',
            'currency': 'currency',
        }
    },
    'sales_agent': {
        'path': 'sales-agent',
        'type': 'object',
        'fields': {
            'phone': 'phone',
            'organization': 'organization',
            'url': 'url',
            'category': 'category',
            'photo': 'photo',
        }
    },
    'rooms': {
        'path': 'rooms',
        'type': 'text',
    },
    'new_flat': {
        'path': 'new-flat',
        'type': 'text',
    },
    'floor': {
        'path': 'floor',
        'type': 'text',
    },
    'floors_total': {
        'path': 'floors-total',
        'type': 'text',
    },
    'building': {
        'path': '.',
        'type': 'object',
        'fields': {
            'name': 'building-name',
            'yandex_building_id': 'yandex-building-id',
            'yandex_house_id': 'yandex-house-id',
            'section': 'building-section',
            'state': 'building-state',
            'ready_quarter': 'ready-quarter',
            'built_year': 'built-year',
            'phase': 'building-phase',
        }
    },
    'images': {
        'path': 'image',
        'type': 'list',
        'fields': {
            'url': '.'
        }
    },
    'description': {
        'path': 'description',
        'type': 'text',
    },
    'area': {
        'path': 'area',
        'type': 'object',
        'fields': {
            'value': 'value',
            'unit': 'unit',
        }
    },
    'living_space': {
        'path': 'living-space',
        'type': 'object',
        'fields': {
            'value': 'value',
            'unit': 'unit',
        }
    },
    'kitchen_space': {
        'path': 'kitchen-space',
        'type': 'object',
        'fields': {
            'value': 'value',
            'unit': 'unit',
        }
    },
    'room_spaces': {
        'path': 'room-space',
        'type': 'list',
        'fields': {
            'value': 'value',
            'unit': 'unit',
        }
    }
}
"""Обязательные поля для парсинга фида YANDEX."""

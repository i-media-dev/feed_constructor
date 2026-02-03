import os

from dotenv import load_dotenv

load_dotenv()


# TEST_YANDEX_DICT = {
#     'internal-id': '1',
#     'type': 'продажа',
#     'property-type': 'жилая',
#     'category': 'квартира',
#     'creation-date': '2026-01-19',
#     'location': {
#         'address': 'Рязань, Новаторов, д.2, кв 7',
#         'latitude': '1251514',
#         'longitude': '12414124',
#         'metro': [
#             {
#                 'name': 'Метро имя',
#                 'time-on-foot': '10',
#                 'time-on-transport': '5'
#             },
#             {
#                 'name': 'Метро фамилия',
#                 'time-on-foot': '15',
#                 'time-on-transport': '5'
#             },
#         ],
#     },
#     'sales-agent': {
#         'category': 'agency',
#         'phone': [
#             '1214151515151',
#             '1241251512142'
#         ]
#     },
#     'price': {
#         'value': '124124214',
#         'currency': 'RUB'
#     },
#     'area': {
#         'value': '50',
#         'unit': 'кв. м'
#     },
#     'rooms': '1',
#     'rooms-offered': '1',
#     'floor': '2',
# }

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

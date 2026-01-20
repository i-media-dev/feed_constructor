import os

from dotenv import load_dotenv

load_dotenv()


SIMPLE_FIELDS = (
    'type',
    'property-type',
    'category',
    'creation-date',
    'rooms',
    'floor',
)

DICT_FIELDS = (
    'location',
    'price',
    'area',
    'sales-agent',
)

LIST_FIELDS = (
    'metro',
    'phone',
)

TEST_YANDEX_DICT = {
    'internal-id': '1',
    'type': 'продажа',
    'property-type': 'жилая',
    'category': 'квартира',
    'creation-date': '2026-01-19',
    'location': {
        'address': 'Рязань, Новаторов, д.2, кв 7',
        'latitude': '1251514',
        'longitude': '12414124',
        'metro': [
            {
                'name': 'Метро имя',
                'time-on-foot': '10',
                'time-on-transport': '5'
            },
            {
                'name': 'Метро фамилия',
                'time-on-foot': '15',
                'time-on-transport': '5'
            },
        ],
    },
    'sales-agent': {
        'category': 'agency',
        'phone': [
            '1214151515151',
            '1241251512142'
        ]
    },
    'price': {
        'value': '124124214',
        'currency': 'RUB'
    },
    'area': {
        'value': '50',
        'unit': 'кв. м'
    },
    'rooms': '1',
    'rooms-offered': '1',
    'floor': '2',
}

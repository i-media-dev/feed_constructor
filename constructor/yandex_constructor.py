import logging

from constructor.domain_model import RealtyObject
from constructor.exceptions import RequiredFieldsError
from constructor.logging_config import setup_logging

setup_logging()


class YandexDictConstructor:

    def __init__(self, obj: RealtyObject):
        self.obj = obj

    def _get_type_deal(self):
        if not self.obj.deal and not self.obj.deal.deal_type:
            raise RequiredFieldsError('Отсутствуют обязательные поля сделки')
        deal_type = 'продажа'
        if self.obj.deal.deal_type.value == 'rent':
            deal_type = 'аренда'
        return deal_type

    def _get_property(self):
        if not self.obj.object_type:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля типа объекта'
            )
        property_type = 'нежилая'
        if self.obj.object_type.value not in ('lot', 'commercial'):
            property_type = 'жилая'
        return property_type

    def _get_location(self):
        if not self.obj.address:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля для контактов'
            )
        return {
            'address':,
            'latitude':,
            'longitude',
            'metro':,
        }

    def get_required_fields(self):
        try:
            return {
                'type': self._get_type_deal(),
                'property-type': self._get_property(),
                'category': self.obj.object_type.value,
                'creation-date': self.obj.created_at,
                'location':,
                'sales-agent':,
                'phone':,
                'category':,
                'price':,
                'value':,
                'currency':,
                'period':,
                'deal-status':,
                'area':,
                'room-space':,
                'living-space':,
                'image':,
                'rooms':,
                'rooms-offered':,
                'floor':,
                'room-furniture':,
                'yandex-building-id':, # специфичные поля (нужно что-то вроде бд или таблицы соответстий)
                'yandex-house-id':, # специфичные поля (нужно что-то вроде бд или таблицы соответстий)
                'built-year':,
            }
        except RequiredFieldsError:
            raise
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

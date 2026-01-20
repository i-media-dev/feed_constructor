import logging

from constructor.domain_model import RealtyObject
from constructor.exceptions import RequiredFieldsError
from constructor.logging_config import setup_logging

setup_logging()


class YandexDictConstructor:

    def __init__(self, obj: RealtyObject):
        self.obj = obj

    def _get_address(self):
        if not self.obj.address:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля для адреса'
            )
        country = self.obj.address.country if self.obj.address.country else ''
        region = self.obj.address.region if self.obj.address.region else ''
        city = self.obj.address.city if self.obj.address.city else ''
        district = (
            self.obj.address.district if self.obj.address.district else ''
        )
        street = self.obj.address.street if self.obj.address.street else ''
        block = self.obj.address.block if self.obj.address.block else ''
        apartment = (
            self.obj.address.apartment if self.obj.address.apartment else ''
        )
        address = (
            f'{country} {region} {city} '
            f'{district} {street} {block} {apartment}'
        )
        if address == '':
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля для адреса'
            )

        return ', '.join(address.split())

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
        if not self.obj.address or not self.obj.address.geo:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля для контактов'
            )
        metros = []
        for metro in self.obj.address.undergrounds or []:
            metros.append({
                'name': metro.name,
                'time-on-foot': metro.time_walk,
                'time-on-transport': metro.time_transport,
            })

        return {
            'address': self._get_address(),
            'latitude': self.obj.address.geo.latitude,
            'longitude': self.obj.address.geo.longitude,
            'metro': metros
        }

    def _get_sales_agent_info(self):
        if not self.obj.contacts or not self.obj.contacts.phones:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля агента'
            )
        return {
            'category': 'agency',
            'phone': [
                f'{phone.country_code}{phone.number}'
                for phone in self.obj.contacts.phones
            ]
        }

    def _get_price(self):
        if not self.obj.deal or not self.obj.deal.rent or not \
                self.obj.deal.rent.price or not self.obj.deal.rent.currency:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля цены'
            )
        return {
            'value': self.obj.deal.rent.price,
            'currency': self.obj.deal.rent.currency
        }

    def _get_area(self):
        if not self.obj.flat or not self.obj.flat.total_area:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля площади'
            )
        return {
            'value': self.obj.flat.total_area,
            'unit': 'кв. м'
        }

    def _get_created_date(self):
        if self.obj.created_at:
            raise RequiredFieldsError(
                'Отсутствуют обязательное поля даты создания объявления'
            )
        return self.obj.created_at

    def _get_rooms(self):
        if not self.obj.flat or not self.obj.flat.rooms_count:
            raise RequiredFieldsError(
                'Отсутствуют обязательное поле комнат'
            )
        return self.obj.flat.rooms_count

    def _get_floor(self):
        if not self.obj.flat or not self.obj.flat.floor:
            raise RequiredFieldsError(
                'Отсутствуют обязательное поле этажа'
            )
        return self.obj.flat.floor

    def _get_id(self):
        if not self.obj.id:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля для контактов'
            )
        return self.obj.id

    def get_required_fields(self):
        try:
            return {
                'internal-id': self._get_id(),
                'type': self._get_type_deal(),
                'property-type': self._get_property(),
                'category': self.obj.object_type.value,
                'creation-date': self._get_created_date(),
                'location': self._get_location(),
                'sales-agent': self._get_sales_agent_info(),
                'price': self._get_price(),
                'area': self._get_area(),
                'rooms': self._get_rooms(),
                'rooms-offered': self._get_rooms(),
                'floor': self._get_floor(),
                # 'yandex-building-id':, # специфичные поля (нужно что-то таблицы соответстий)
                # 'yandex-house-id':, # специфичные поля (нужно что-то таблицы соответстий)
                # 'built-year':,
            }
        except RequiredFieldsError:
            raise
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

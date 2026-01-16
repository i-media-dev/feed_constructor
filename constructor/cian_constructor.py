import logging

from constructor.domain_model import RealtyObject
from constructor.exceptions import RequiredFieldsError
from constructor.logging_config import setup_logging

setup_logging()


class CianDictConstructor:

    def __init__(self, obj: RealtyObject):
        self.obj = obj

    def _get_category(self):
        if not self.obj.object_type or not self.obj.deal.deal_type:
            raise RequiredFieldsError('Не указан тип объекта или тип сделки')

        object_type = self.obj.object_type.value
        deal_type = self.obj.deal.deal_type.value.capitalize()

        return f'{object_type}{deal_type}'

    def _get_adress(self):
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

    def _get_phones(self):
        if not self.obj.contacts or not self.obj.contacts.phones:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля для контактов'
            )
        return [
            {
                'CountryCode': phone.country_code,
                'Number': phone.number
            } for phone in self.obj.contacts.phones
        ]

    def get_required_fields(self):
        try:
            return {
                'Category': self._get_category(),
                'ExternalId': self.obj.id,
                'Description': self.obj.description,
                'Address': self._get_adress(),
                'FlatRoomsCount': self.obj.flat.rooms_count,
                'Phones': self._get_phones(),
                'TotalArea': self.obj.flat.total_area,
            }
        except RequiredFieldsError:
            raise
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

import logging

from constructor.models.model_new_flat import NewFlatObject
from constructor.settings.logging_config import setup_logging

setup_logging()


class CianNewFlatConstructor:
    AGENT_BONUS = 1
    SALE_TYPE = 'Свободная продажа'
    PERSONE_TYPE = 'Юридическое лицо'
    CATEGORY = 'Квартира в новостройке'

    def __init__(self, objects: list[NewFlatObject]):
        self.objects = objects

    def _get_address(self, obj: NewFlatObject):
        if not obj.complex or not obj.complex.address:
            return

        country = obj.complex.address.country \
            if obj.complex.address.country else ''
        region = obj.complex.address.region \
            if obj.complex.address.region else ''
        city = obj.complex.address.city if obj.complex.address.city else ''
        street = obj.complex.address.street \
            if obj.complex.address.street else ''
        block = obj.complex.address.block if obj.complex.address.block else ''

        address = (
            f'{country} {region} {city} '
            f'{street} {block}'
        )
        if address == '':
            return

        return ', '.join(address.split())

    def _get_phones(self, obj: NewFlatObject):
        if not obj.seller or not obj.seller.phones:
            return {}
        return {
            'PhoneSchema': [
                {
                    'CountryCode': phone.country_code,
                    'Number': phone.number
                } for phone in obj.seller.phones
            ]
        }

    def _get_description(self, obj: NewFlatObject) -> str:
        parts = []

        if obj.description:
            parts.append(obj.description)

        if obj.complex and obj.complex.description:
            parts.append(obj.complex.description)

        return '\n\n'.join(parts)

    def _get_id(self, obj: NewFlatObject):
        if not obj.id:
            return
        return obj.id

    def _get_area(self, obj: NewFlatObject):
        if not obj.areas or not obj.areas.total:
            return
        return obj.areas.total

    def _get_photos(self, obj: NewFlatObject):
        if not obj.media or not obj.media.photos:
            return {}
        return {
            'PhotoSchema': [
                {
                    'FullUrl': photo.url,
                    'IsDefault': photo.is_default
                } for photo in obj.media.photos
            ]
        }

    def _get_videos(self, obj: NewFlatObject):
        if not obj.media or not obj.media.videos:
            return {}
        return {
            'VideoSchema': {
                'Url': obj.media.videos
            }
        }

    def _get_email(self, obj: NewFlatObject):
        if not obj.seller or not obj.seller.email:
            return
        return obj.seller.email

    def _get_cplmoderation(self):
        return {'PersonType': self.PERSONE_TYPE}

    def _get_building_info(self, obj: NewFlatObject):
        if not obj.building or not obj.building.floors_total:
            return
        return {'FloorsCount': obj.building.floors_total}

    def _get_bargainterms(self, obj: NewFlatObject):
        if not obj.sale or not obj.sale.price:
            return {}
        return {
            'Price': obj.sale.price,
            'SaleType': self.SALE_TYPE,
            'AgentBonus': {
                'Value': self.AGENT_BONUS
            }
        }

    def _get_jk_info(self, obj: NewFlatObject):
        if not obj.complex or not obj.complex.id or not obj.complex.name \
                or not obj.building.id:
            return
        return {
            'Id': obj.complex.id,
            'Name': obj.complex.name,
            'House':
                {
                    'Id': obj.building.id,
                }
        }

    def structure_fields(self, obj: NewFlatObject):
        try:
            return {
                'Category': self.CATEGORY,
                'ExternalId': self._get_id(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def info_fields(self, obj: NewFlatObject):
        try:
            return {
                'Description': self._get_description(obj),
                'Address': self._get_address(obj),
                'FlatRoomsCount': obj.rooms,
                'TotalArea': self._get_area(obj),
                'FloorNumber': obj.floor,
                'JKSchema': self._get_jk_info(obj),
                'Building': self._get_building_info(obj),
                'BargainTerms': self._get_bargainterms(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def law_fields(self):
        try:
            return {
                'CplModeration': self._get_cplmoderation()
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def contact_fields(self, obj: NewFlatObject):
        try:
            return {
                'Phones': self._get_phones(obj),
                'Email': self._get_email(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def media_fields(self, obj: NewFlatObject):
        try:
            return {
                'Photos': self._get_photos(obj),
                'Videos': self._get_videos(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def build(self) -> list[dict]:
        result = []

        for obj in self.objects:
            item = {}
            item.update(self.structure_fields(obj))
            item.update(self.info_fields(obj))
            item.update(self.law_fields())
            item.update(self.contact_fields(obj))
            item.update(self.media_fields(obj))

            result.append(item)

        return result

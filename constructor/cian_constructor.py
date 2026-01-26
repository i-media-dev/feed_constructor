import logging

from constructor.domain_model import RealtyObject
from constructor.logging_config import setup_logging

setup_logging()


class CianDictConstructor:

    def __init__(self, objects: list[RealtyObject]):
        self.objects = objects

    def _get_category(self, obj: RealtyObject):
        if not obj.object_type or not obj.deal.deal_type:
            return

        object_type = obj.object_type.value
        deal_type = obj.deal.deal_type.value.capitalize()

        return f'{object_type}{deal_type}'

    def _get_address(self, obj: RealtyObject):
        if not obj.address:
            return

        country = obj.address.country if obj.address.country else ''
        region = obj.address.region if obj.address.region else ''
        city = obj.address.city if obj.address.city else ''
        district = (
            obj.address.district if obj.address.district else ''
        )
        street = obj.address.street if obj.address.street else ''
        block = obj.address.block if obj.address.block else ''
        apartment = (
            obj.address.apartment if obj.address.apartment else ''
        )
        address = (
            f'{country} {region} {city} '
            f'{district} {street} {block} {apartment}'
        )
        if address == '':
            return

        return ', '.join(address.split())

    def _get_phones(self, obj: RealtyObject):
        if not obj.contacts or not obj.contacts.phones:
            return
        return {
            'PhoneSchema': [
                {
                    'CountryCode': phone.country_code,
                    'Number': phone.number
                } for phone in obj.contacts.phones
            ]
        }

    def _get_description(self, obj: RealtyObject):
        if not obj.description:
            return
        return obj.description

    def _get_id(self, obj: RealtyObject):
        if not obj.id:
            return
        return obj.id

    def _get_rooms(self, obj: RealtyObject):
        if not obj.flat or not obj.flat.rooms_count:
            return
        return obj.flat.rooms_count

    def _get_area(self, obj: RealtyObject):
        if not obj.flat or not obj.flat.total_area:
            return
        return obj.flat.total_area

    def _get_floor(self, obj: RealtyObject):
        if not obj.flat or not obj.flat.floor:
            return
        return obj.flat.floor

    def _get_email(self, obj: RealtyObject):
        if not obj.contacts or not obj.contacts.contact_email:
            return
        return obj.contacts.contact_email

    def _get_photos(self, obj: RealtyObject):
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

    def _get_videos(self, obj: RealtyObject):
        if not obj.media or not obj.media.videos:
            return {}
        return {
            'VideoSchema': {
                'Url': obj.media.videos
            }
        }

    def _get_cplmoderation(self):
        return {'PersonType': 'Юридическое лицо'}

    def _get_building_info(self, obj: RealtyObject):
        if not obj.building or not obj.building.floors_total:
            return
        return {'FloorsCount': obj.building.floors_total}

    def _get_bargainterms(self, obj: RealtyObject):
        if not obj.deal or not obj.deal.rent or not obj.deal.rent.price:
            return
        return {
            'Price': obj.deal.rent.price,
            'SaleType': 'Свободная продажа',
            'AgentBonus': {
                'Value': obj.deal.rent.agent_fee_percent
            }
        }

    def _get_jk_info(self, obj: RealtyObject):
        if not obj.building or not obj.building.jk_name:
            return
        return {
            'Id': '',
            'Name': obj.building.jk_name,
            'House':
                {
                    'Id': '',
                }
        }

    def get_structure_fields(self, obj: RealtyObject):
        try:
            return {
                'Category': self._get_category(obj),
                'ExternalId': self._get_id(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def get_info_fields(self, obj: RealtyObject):
        try:
            return {
                'Description': self._get_description(obj),
                'Address': self._get_address(obj),
                'FlatRoomsCount': self._get_rooms(obj),
                'TotalArea': self._get_area(obj),
                'FloorNumber': self._get_floor(obj),
                'JKSchema': self._get_jk_info(obj),
                'Building': self._get_building_info(obj),
                'BargainTerms': self._get_bargainterms(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def get_law_fields(self):
        try:
            return {
                'CplModeration': self._get_cplmoderation()
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def get_contact_fields(self, obj: RealtyObject):
        try:
            return {
                'Phones': self._get_phones(obj),
                'Email': self._get_email(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def get_media_fields(self, obj: RealtyObject):
        try:
            return {
                'Photos': self._get_photos(obj),
                'Videos': self._get_videos(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def dict_constructor(self) -> list[dict]:
        result = []

        for obj in self.objects:
            item = {}
            item.update(self.get_structure_fields(obj))
            item.update(self.get_info_fields(obj))
            item.update(self.get_law_fields())
            item.update(self.get_contact_fields(obj))
            item.update(self.get_media_fields(obj))

            result.append(item)

        return result

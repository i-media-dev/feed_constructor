import logging

from constructor.logging_config import setup_logging
from constructor.model_new_flat import NewFlatObject
from constructor.model_seller import Seller

setup_logging()


class YandexNewFlatConstructor:
    TYPE = 'продажа'
    PROPERTY_TYPE = 'жилая'
    CATEGORY = 'квартира'
    COUNTRY = 'Россия'
    UNIT_AREA = 'кв. м'

    def __init__(self, objects: list[NewFlatObject], seller: Seller):
        self.objects = objects
        self.seller = seller

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

    def _get_description(self, obj: NewFlatObject) -> str:
        parts = []

        if obj.description:
            parts.append(obj.description)

        if obj.complex.description:
            parts.append(obj.complex.description)

        return '\n\n'.join(parts)

    def _get_location(self, obj: NewFlatObject):
        if not obj.complex or not obj.complex.address \
                or not obj.complex.address.geo:
            return {}
        metros = []
        for metro in obj.complex.address.undergrounds or []:
            metros.append({
                'name': metro.name,
                'time-on-foot': metro.walk_time_minutes,
                'time-on-transport': metro.transport_time_minutes,
            })

        return {
            'address': self._get_address(obj),
            'latitude': obj.complex.address.geo.latitude,
            'longitude': obj.complex.address.geo.longitude,
            'metro': metros
        }

    def _get_sales_agent_info(self):
        if not self.seller.phones or not self.seller.category:
            return {}
        return {
            'name': self.seller.name,  # не обязательное
            'phone': [
                f'{phone.country_code}{phone.number}'
                for phone in self.seller.phones
            ],
            'category': self.seller.category.value,
            'organization': self.seller.organization,  # не обязательное
            'url': self.seller.url,  # не обязательное
            'photo': self.seller.photo_url  # не обязательное
        }

    def _get_price(self, obj: NewFlatObject):
        if not obj.sale or not obj.sale.price or not obj.sale.currency:
            return {}
        return {
            'value': obj.sale.price,
            'currency': obj.sale.currency
        }

    def _get_deal_status(self):
        if not self.seller.category:
            return
        deal_status = 'прямая продажа'
        if self.seller.category == 'developer':
            deal_status = 'продажа от застройщика'
        return deal_status

    def _get_area(self, obj: NewFlatObject):
        if not obj.areas or not obj.areas.total:
            return {}
        return {
            'value': obj.areas.total,
            'unit': self.UNIT_AREA
        }

    def _get_living_area(self, obj: NewFlatObject):
        if not obj.areas or not obj.areas.living:
            return
        return {
            'value': obj.areas.living,
            'unit': self.UNIT_AREA
        }

    def _get_images(self, obj: NewFlatObject):
        if not obj.media or not obj.media.photos:
            return []
        return [
            photo.url for photo in obj.media.photos
        ]

    def _get_floor_total(self, obj: NewFlatObject):
        if not obj.building or not obj.building.floors_total:
            return
        return obj.building.floors_total

    def _get_building_name(self, obj: NewFlatObject):
        if not obj.building or not obj.building.name:
            return
        return obj.building.name

    def _get_yandex_building_id(self, obj: NewFlatObject):
        pass

    def _get_yandex_house_id(self, obj: NewFlatObject):
        pass

    def _get_built_state(self, obj: NewFlatObject):
        if not obj.building or not obj.building.built:
            return
        built_state = 'unfinished'
        if obj.building.built:
            built_state = 'hand-over'
        return built_state

    def _get_quarter(self, obj: NewFlatObject):
        if not obj.complex or not obj.complex.completion_quarter:
            return
        return obj.complex.completion_quarter

    def _get_built_year(self, obj: NewFlatObject):
        if not obj.complex or not obj.complex.completion_year:
            return
        return obj.complex.completion_year

    def general_info(self, obj: NewFlatObject):
        try:
            return {
                'internal-id': obj.id,
                'type': self.TYPE,
                'property-type': self.PROPERTY_TYPE,
                'category': self.CATEGORY,
                'creation-date': obj.created_at,
                'location': self._get_location(obj),
                'country': self.COUNTRY
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def seller_info(self, obj: NewFlatObject):
        try:
            return {
                'sales-agent': self._get_sales_agent_info(),
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def dael_info(self, obj: NewFlatObject):
        try:
            return {
                'deal-status': self._get_deal_status(),
                'price': self._get_price(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def object_info(self, obj: NewFlatObject):
        try:
            return {
                'image': self._get_images(obj),
                'area': self._get_area(obj),
                'living-space': self._get_living_area(obj),
                'description': self._get_description(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def flat_info(self, obj: NewFlatObject):
        try:
            return {
                'new-flat': 'да',
                'floor': obj.floor,
                'rooms': obj.rooms
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def building_info(self, obj: NewFlatObject):
        try:
            return {
                'floors-total': self._get_floor_total(obj),
                'building-name': self._get_building_name(obj),
                'yandex-building-id': self._get_yandex_building_id(obj),
                'yandex-house-id': self._get_yandex_house_id(obj),
                'building-state': self._get_built_state(obj),
                'built-year': self._get_built_year(obj),
                'ready-quarter': self._get_quarter(obj)
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def build(self) -> list[dict]:
        result = []

        for obj in self.objects:
            item = {}
            item.update(self.general_info(obj))
            item.update(self.seller_info(obj))
            item.update(self.dael_info(obj))
            item.update(self.object_info(obj))
            item.update(self.flat_info(obj))
            item.update(self.building_info(obj))

            result.append(item)

        return result

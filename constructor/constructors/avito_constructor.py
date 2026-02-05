import logging

from constructor.models.model_new_flat import NewFlatObject
from constructor.settings.logging_config import setup_logging

setup_logging()


class AvitoNewFlatConstructor:
    CATEGORY = 'Квартиры'
    OPERATION = 'Продам'
    MARKET_TYPE = 'Новостройка'

    def __init__(self, objects: list[NewFlatObject]):
        self.objects = objects

    def _get_price(self, obj: NewFlatObject):
        if not obj.sale or not obj.sale.price:
            return
        return obj.sale.price

    def _get_description(self, obj: NewFlatObject) -> str:
        parts = []

        if obj.description:
            parts.append(obj.description)

        if obj.complex and obj.complex.description:
            parts.append(obj.complex.description)

        return '\n\n'.join(parts)

    def _get_house_type(self, obj: NewFlatObject):
        if not obj.building or not obj.building.building_material:
            return
        return obj.building.building_material

    def _get_floors(self, obj: NewFlatObject):
        if not obj.building or not obj.building.floors_total:
            return
        return obj.building.floors_total

    def _get_area(self, obj: NewFlatObject):
        if not obj.areas or not obj.areas.total:
            return
        return obj.areas.total

    def _get_development_id(self, obj: NewFlatObject):
        pass

    def _get_property_rights(self, obj: NewFlatObject):
        if not obj.seller or not obj.seller.category:
            return
        seller = obj.seller.category.value
        if seller == 'owner':
            return 'Собственник'
        if seller == 'developer':
            return 'Застройщик'
        return 'Посредник'

    def _get_decoration(self, obj: NewFlatObject):
        if not obj.decoration:
            return
        if obj.decoration.value == 'finishing':
            return 'Чистовая'
        if obj.decoration.value == 'pre_finishing':
            return 'Предчистовая'
        return 'Без отделки'

    def _get_images(self, obj: NewFlatObject):
        if not obj.media or not obj.media.photos:
            return []
        return {'Image url=': [photo.url for photo in obj.media.photos]}

    def identity_fields(self, obj: NewFlatObject):
        try:
            return {
                'Id': obj.id,
                'Category': self.CATEGORY,
                'OperationType': self.OPERATION,
                'MarketType': self.MARKET_TYPE,
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def flat_fields(self, obj: NewFlatObject):
        try:
            return {
                'Rooms': obj.rooms,
                'Square': self._get_area(obj),
                'Floor': obj.floor,
                'Floors': self._get_floors(obj),
                'Decoration': self._get_decoration(obj),
                'Status': obj.type_flat,
                'HouseType': self._get_house_type(obj),
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def development_fields(self, obj: NewFlatObject):
        try:
            return {
                'NewDevelopmentId': self._get_development_id(obj),
                'PropertyRights': self._get_property_rights(obj),
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def deal_fields(self, obj: NewFlatObject):
        try:
            return {
                'Price': self._get_price(obj),
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def content_fields(self, obj: NewFlatObject):
        try:
            return {
                'Description': self._get_description(obj),
                'Images': self._get_images(obj),
            }
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

    def build(self):
        result = []

        for obj in self.objects:
            item = {}
            item.update(self.identity_fields(obj))
            item.update(self.flat_fields(obj))
            item.update(self.development_fields(obj))
            item.update(self.deal_fields(obj))
            item.update(self.content_fields(obj))

            result.append(item)

        return result

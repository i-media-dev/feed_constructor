import logging

from constructor.avito_constants import CATEGORIES_REALTY, TYPE_OF_DEAL
from constructor.domain_model import RealtyObject
from constructor.exceptions import RequiredFieldsError
from constructor.logging_config import setup_logging

setup_logging()


class AvitoDictConstructor:

    def __init__(self, obj: RealtyObject):
        self.obj = obj

    def _get_category(self):
        if not self.obj.object_type:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля категорий'
            )
        return CATEGORIES_REALTY.get(self.obj.object_type.value, 'Неизвестно')

    def _get_operation_type(self):
        if not self.obj.deal or not self.obj.deal.deal_type:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля категорий'
            )
        return TYPE_OF_DEAL.get(self.obj.deal.deal_type.value, 'Неизвестно')

    def _get_price(self):
        if not self.obj.deal or not self.obj.deal.rent \
                or not self.obj.deal.rent.price:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля цены'
            )
        return self.obj.deal.rent.price

    def _get_description(self):
        if not self.obj.description:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля описания'
            )
        return self.obj.description

    def _get_market_type(self):
        if not self.obj.building or not self.obj.building.building_type:
            raise RequiredFieldsError(
                'Отсутствуют обязательное поле типа постройки'
            )
        return self.obj.building.building_type

    def _get_house_type(self):
        if not self.obj.building or not self.obj.building.building_material:
            raise RequiredFieldsError(
                'Отсутствуют обязательное поле материала постройки'
            )
        return self.obj.building.building_material

    def _get_floor(self):
        if not self.obj.flat or not self.obj.flat.floor:
            raise RequiredFieldsError(
                'Отсутствуют обязательное поле этажа'
            )
        return self.obj.flat.floor

    def _get_rooms(self):
        if not self.obj.flat or not self.obj.flat.rooms_count:
            raise RequiredFieldsError(
                'Отсутствуют обязательное поле комнат'
            )
        return self.obj.flat.rooms_count

    def _get_floors(self):
        if not self.obj.flat or not self.obj.flat.floors_total:
            raise RequiredFieldsError(
                'Отсутствуют обязательное поле этажности строения'
            )
        return self.obj.flat.floors_total

    def _get_area(self):
        if not self.obj.flat or not self.obj.flat.total_area:
            raise RequiredFieldsError(
                'Отсутствуют обязательное поле площади жилого помещения'
            )
        return self.obj.flat.total_area

    def _get_id(self):
        if not self.obj.id:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля для контактов'
            )
        return self.obj.id

    def get_required_fields(self):
        try:
            return {
                'id': self._get_id(),
                'Description': self._get_description(),
                'Category': self._get_category(),
                'OperationType': self._get_operation_type(),
                'Price': self._get_price(),
                'MarketType': self._get_market_type(),
                'HouseType': self._get_house_type(),
                'Floor': self._get_floor(),
                'Floors': self._get_floors(),
                'Square': self._get_area(),
                'Status': 'Квартира',
            }
        except RequiredFieldsError:
            raise
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

import logging

from constructor.domain_model import RealtyObject
from constructor.exceptions import RequiredFieldsError
from constructor.logging_config import setup_logging
from constructor.avito_constants import CATEGORIES_REALTY, TYPE_OF_DEAL

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
                'Отсутствуют обязательные поля типа постройки'
            )
        return self.obj.building.building_type

    def _get_house_type(self):
        if not self.obj.building or not self.obj.building.building_material:
            raise RequiredFieldsError(
                'Отсутствуют обязательные поля типа постройки'
            )
        return self.obj.building.building_material

    def get_required_fields(self):
        try:
            return {
                'id': '1',
                'Description': self._get_description(),
                'Category': self._get_category(),
                'OperationType': self._get_operation_type(),
                'Price': self._get_price(),
                'MarketType': self._get_market_type(),
                'HouseType': self._get_house_type(),
                'Floor':,
                'Floors':,
                'Rooms':,
                'Square':,
                'Status':,
            }
        except RequiredFieldsError:
            raise
        except Exception as error:
            logging.error('Неожиданная ошибка: %s', error)
            raise

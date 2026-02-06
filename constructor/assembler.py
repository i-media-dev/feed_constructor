import logging
from abc import ABC, abstractmethod

from constructor.constants.avito_constants import AVITO_SELLER_MAP
from constructor.constants.cian_constants import CIAN_SELLER_MAP, CIAN_CURRENCY_MAP
from constructor.constants.yandex_constants import YANDEX_SELLER_MAP
from constructor.models.model_new_flat import (Address, Building, Currency,
                                               DecorationType,
                                               DeveloperContacts, FlatAreas,
                                               Geo, Media, NewFlatObject,
                                               Phone, Photo,
                                               ResidentialComplex,
                                               ResidentialComplexClass,
                                               SaleInfo, Underground)
from constructor.models.model_seller import Seller, SellerCategory, SellerPhone
from constructor.settings.logging_config import setup_logging

setup_logging()


class NewFlatAssembler(ABC):

    def __init__(self, data: list[dict]):
        self.data = data

    @abstractmethod
    def _build_currency(self, obj):
        pass

    @abstractmethod
    def _build_sale_info(self, obj):
        pass

    @abstractmethod
    def _build_geo(self, obj):
        pass

    @abstractmethod
    def _build_underground(self, obj):
        pass

    @abstractmethod
    def _address(self, obj):
        pass

    @abstractmethod
    def _build_rc_class(self, obj):
        pass

    @abstractmethod
    def _build_decoration(self, obj):
        pass

    @abstractmethod
    def _residential_complex(self, obj):
        pass

    @abstractmethod
    def _build_building(self, obj):
        pass

    @abstractmethod
    def _build_areas(self, obj):
        pass

    @abstractmethod
    def _build_photo(self, obj):
        pass

    @abstractmethod
    def _build_media(self, obj):
        pass

    @abstractmethod
    def _build_flat(self, obj):
        pass

    @abstractmethod
    def _build_seller_category(self, obj):
        pass

    @abstractmethod
    def _build_phone(self, obj):
        pass

    @abstractmethod
    def _build_seller(self, obj):
        pass

    def assemble(self):
        result = []
        try:
            for obj in self.data:

                result.append(flat)
        except Exception as error:
            logging.error('Неожиданная ошибка при сборке модели: %s', error)
        return result


class AvitoNewFlatAssembler(NewFlatAssembler):
    pass


class CianNewFlatAssembler(NewFlatAssembler):

    def _build_currency(self, data: dict):
        bargain_terms = data.get('bargain_terms')
        if bargain_terms:
            return Currency(
                CIAN_CURRENCY_MAP.get(bargain_terms.get('currency'))
            )

    def _build_sale_info(self, data: dict):
        bargain_terms = data.get('bargain_terms')
        if bargain_terms:
            return SaleInfo(
                price=bargain_terms.get('price'),
                currency=self._build_currency(data)
            )

    def _build_geo(self, data: dict):
        return Geo()

    def _build_underground(self, data: dict):
        return Underground()

    def _address(self, data: dict):
        return Address(
            raw_address=data.get('address')
        )

    def _build_rc_class(self, data: dict):
        return ResidentialComplexClass(

        )

    def _build_decoration(self, data: dict):
        pass

    def _residential_complex(self, data: dict):
        pass

    def _build_building(self, data: dict):
        pass

    def _build_areas(self, data: dict):
        pass

    def _build_photo(self, data: dict):
        pass

    def _build_media(self, data: dict):
        pass

    def _build_flat(self, data: dict):
        pass

    def _build_seller_category(self, data: dict):
        pass

    def _build_phone(self, data: dict):
        pass

    def _build_seller(self, data: dict):
        pass


class YandexNewFlatAssembler(NewFlatAssembler):
    pass

import logging
from abc import ABC, abstractmethod

from constructor.constants.avito_constants import AVITO_SELLER_MAP
from constructor.constants.cian_constants import CIAN_SELLER_MAP
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
    def _geo(self, obj):
        pass

    @abstractmethod
    def _underground(self):
        pass

    @abstractmethod
    def _address(self):
        pass

    @abstractmethod
    def _build_rc_class(self):
        pass

    @abstractmethod
    def _build_decoration(self):
        pass

    @abstractmethod
    def _residential_complex(self):
        pass

    @abstractmethod
    def _build_building(self):
        pass

    @abstractmethod
    def _build_areas(self):
        pass

    @abstractmethod
    def _build_photo(self):
        pass

    @abstractmethod
    def _build_media(self):
        pass

    @abstractmethod
    def _build_flat(self):
        pass

    @abstractmethod
    def _build_seller_category(self):
        pass

    @abstractmethod
    def _build_phone(self):
        pass

    @abstractmethod
    def _build_seller(self):
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

    @abstractmethod
    def _build_currency(self, data: dict):
        person_type = data.get('bargain_terms')
        return Currency(
            AVITO_SELLER_MAP.get(bargain_terms.get(''))
        )

    @abstractmethod
    def _build_sale_info(self):
        pass

    @abstractmethod
    def _geo(self):
        pass

    @abstractmethod
    def _underground(self):
        pass

    @abstractmethod
    def _address(self):
        pass

    @abstractmethod
    def _build_rc_class(self):
        pass

    @abstractmethod
    def _build_decoration(self):
        pass

    @abstractmethod
    def _residential_complex(self):
        pass

    @abstractmethod
    def _build_building(self):
        pass

    @abstractmethod
    def _build_areas(self):
        pass

    @abstractmethod
    def _build_photo(self):
        pass

    @abstractmethod
    def _build_media(self):
        pass

    @abstractmethod
    def _build_flat(self):
        pass

    @abstractmethod
    def _build_seller_category(self):
        pass

    @abstractmethod
    def _build_phone(self):
        pass

    @abstractmethod
    def _build_seller(self):
        pass


class YandexNewFlatAssembler(NewFlatAssembler):
    pass

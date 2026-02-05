import logging
from abc import ABC, abstractmethod

from constructor.models.model_new_flat import NewFlatObject, Phone
from constructor.models.model_seller import Seller
from constructor.settings.logging_config import setup_logging

setup_logging()


class PhoneBuilder:
    @staticmethod
    def build_list(data):
        return [Phone(**phone) for phone in data.get('phones', [])]


class SellerBuilder:
    @staticmethod
    def build(data: dict) -> Seller:
        return Seller(
            name=,
            category=,
            phones=,
            organization=,
            url=,
            email=,
            photo_url=,
            payment=,
            external_ids=)


class AvitoNewFlatAssembler():
    pass


class CianNewFlatAssembler():
    pass


class YandexNewFlatAssembler():
    pass

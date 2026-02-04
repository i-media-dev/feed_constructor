import logging

from constructor.models.model_new_flat import NewFlatObject
from constructor.models.model_seller import Seller
from constructor.settings.logging_config import setup_logging

setup_logging()


class NewFlatAssembler:

    def __init__(self, data: list[dict]):
        self.data = data

    def _built(self, data: dict):
        return NewFlatObject(
            id=data[],
            complex=data[],
            building=data[],
            rooms=data[],
            floor=data[],
            areas=data[],
            sale=data[],
            type_flat=data[],
            decoration=data[],
            ceiling_height=data[],
            layout_type=data[],
            media=data[],
            description=data[],
            created_at=data[],
            updated_at=data[]
        )

    def assemble(self):
        result = []
        try:
            for el in self.data:
                obj = self._built(el)
                result.append(obj)
        except Exception as error:
            logging.error('Неожиданная ошибка при сборке модели: %s', error)
        return result

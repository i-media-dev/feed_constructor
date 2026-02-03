from constructor.models.model_new_flat import NewFlatObject
from constructor.models.model_seller import Seller


class ModelAssembler:

    def __init__(self, data: list[dict]):
        self.data = data

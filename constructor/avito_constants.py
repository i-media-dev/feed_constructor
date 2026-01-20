import os

from dotenv import load_dotenv

load_dotenv()

CATEGORIES_REALTY = {
    'flat': 'Квартиры',
    'house': 'Дома',
    'room': 'Комнаты',
    'garage': 'Гаражи',
    'cottage': 'Коттеджи',
    'townhouse': 'Таунхаусы',
}
"""Словарь соответсивий категорий."""

TYPE_OF_DEAL = {
    'rent': 'Сдается',
    'sale': 'Продается'
}
"""Словарь соответствий типа сделок."""

SIMPLE_FIELDS = (
    'id',
    'Description',
    'Category',
    'OperationType',
    'Price',
    'MarketType',
    'HouseType',
    'Floor',
    'Floors',
    'Square',
    'Status',
)

LIST_FIELDS = (
    'Images',
)

TEST_AVITO_DICT = {
    'id': '123',
    'Description': 'баллбафлфалфыафдыладлф фждылаж дфлыждл фды жфдылажфл ыдпж дфлыажд фж',
    'Category': 'Квартиры',
    'OperationType': 'Продажа',
    'Price': '5000000',
    'MarketType': 'Новостройка',
    'HouseType': 'Блочный',
    'Floor': '20',
    'Floors': '21',
    'Square': '38',
    'Status': 'Квартира',
}

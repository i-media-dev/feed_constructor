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

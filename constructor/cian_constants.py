import os

from dotenv import load_dotenv

load_dotenv()

SIMPLE_FIELDS = [
    'Category',
    'ExternalId',
    'Description',
    'Address',
    'FlatRoomsCount',
    'TotalArea'
]
"""Простые поля без вложенности."""

FIELDS_WITH_SCHEMA = [
    'Phones',
    'Photos',
    'Videos',
    'Undergrounds'
]
"""Поля с вложенностью schema."""

SCHEMA_NAMES = {
    'Phones': 'PhoneSchema',
    'Photos': 'PhotoSchema',
    'Videos': 'VideoSchema',
    'Undergrounds': 'UndergroundInfoSchema'
}
"""Поля и название схемы, которое к ним относится."""

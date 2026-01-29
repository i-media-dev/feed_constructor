from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class SellerCategory(Enum):
    """Тип продавца."""
    OWNER = 'owner'  # собственник
    AGENT = 'agent'  # агент
    AGENCY = 'agency'  # агентство
    DEVELOPER = 'developer'  # застройщик
    COMPANY = 'company'  # компания


@dataclass
class SellerPhone:
    """Номер телефона."""
    country_code: str  # код страны
    number: str  # номер телефона


@dataclass
class Seller:
    """
    Универсальная модель продавца / источника объявления.
    """

    name: str  # имя продавца
    category: SellerCategory  # тип продавца
    phones: List[SellerPhone]  # номе телефона

    organization: Optional[str] = None  # юридическое название организации
    url: Optional[str] = None  # ссылка на сайт продавца
    email: Optional[str] = None  # почта

    photo_url: Optional[str] = None  # фото продавца

    payment: Optional[str] = None  # ставка агенту

    external_ids: dict[str, str] = field(default_factory=dict)  # айди

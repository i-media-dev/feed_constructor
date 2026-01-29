from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional


class Currency(Enum):
    """Тип валюты."""
    RUB = 'RUB'  # рубль
    USD = 'USD'  # доллар
    EUR = 'EUR'  # евро


@dataclass
class SaleInfo:
    """Общая информация о продаже."""
    price: float  # цена
    currency: Currency = Currency.RUB  # валюта

    mortgage_available: Optional[bool] = None  # возможна ипотека
    installment_available: Optional[bool] = None  # возможна рассрочка
    trade_in_available: Optional[bool] = None  # возможен обмен


@dataclass
class Phone:
    """Номер телефона."""
    country_code: str  # код страны
    number: str  # номер


@dataclass
class DeveloperContacts:
    """Котнакты застройщика."""
    phones: List[Phone]  # номер телефона застройщика
    email: Optional[str] = None  # почта застройщика
    sales_department_name: Optional[str] = None  # название отдела продаж


@dataclass
class Geo:
    """Координаты."""
    latitude: Optional[float] = None  # широта
    longitude: Optional[float] = None  # долгота


@dataclass
class Underground:
    """Модель информации о метро."""
    name: str

    walk_time_minutes: Optional[int] = None
    transport_time_minutes: Optional[int] = None


@dataclass
class Address:
    """Полный адрес."""
    country: Optional[str] = None  # страна
    region: Optional[str] = None  # область
    city: Optional[str] = None  # город
    street: Optional[str] = None  # улица
    house_number: Optional[str] = None  # номер дома
    block: Optional[str] = None  # район

    geo: Optional[Geo] = None  # координаты

    undergrounds: List[Underground] = field(default_factory=list)  # Метро


class ResidentialComplexClass(Enum):
    """Класс жилого комплекса."""
    ECONOMY = 'economy'  # эконом
    COMFORT = 'comfort'  # комфорт
    BUSINESS = 'business'  # бизнес
    PREMIUM = 'premium'  # премиум


class DecorationType(Enum):
    """Типы отделки."""
    NO_DECORATION = 'no_decoration'  # без отделки
    PRE_FINISHING = 'pre_finishing'  # предчистовая
    FINISHING = 'finishing'  # чистовая


@dataclass
class ResidentialComplex:
    """Информация о жилом комлпексе."""
    id: Optional[str] = None  # id жилого комплекса
    name: Optional[str] = None  # название жилого комплекса

    developer_name: Optional[str] = None  # название застройщика
    contacts: Optional[DeveloperContacts] = None  # контакты застройщика

    address: Optional[Address] = None  # адрес

    # класс жилого комплекса
    class_type: Optional[ResidentialComplexClass] = None

    completion_year: Optional[int] = None  # год постройки
    # квартал заврешения строительства
    completion_quarter: Optional[int] = None

    description: Optional[str] = None  # описание жк


@dataclass
class Building:
    """Информация о постройке."""
    id: str  # айди здания
    complex_id: str  # айди комплекса

    floors_total: int  # этажность

    name: Optional[str] = None  # название
    building_material: Optional[str] = None  # материалы постройки
    parking_type: Optional[str] = None  # тип паркинга

    built: Optional[bool] = None  # True - построен, False - строится


@dataclass
class FlatAreas:
    """Информация о площади квартиры."""
    total: float  # общая площадь
    living: Optional[float] = None  # жилая площадь
    kitchen: Optional[float] = None  # площадь кухни


@dataclass
class Photo:
    """Фото."""
    url: str  # ссылка на фото
    is_default: bool = False  # True - дефолтное фото


@dataclass
class Media:
    """Медиа данные объекта."""
    photos: List[Photo] = field(default_factory=list)  # фотографии
    videos: List[str] = field(default_factory=list)  # видео
    plan: Optional[str] = None  # план квартиры


@dataclass
class NewFlatObject:
    """Моедль с суммарной полной информацией по объекту недвижимости."""
    id: str  # айди

    complex: ResidentialComplex  # жк
    building: Building  # здание

    rooms: int  # количество комнат
    floor: int  # этаж
    areas: FlatAreas  # площадь

    sale: SaleInfo  # информация по продаже

    type_flat: str = 'квартира'

    decoration: Optional[DecorationType] = None  # тип отделки

    ceiling_height: Optional[float] = None  # высота потолков
    layout_type: Optional[str] = None  # планировка

    media: Optional[Media] = None  # медиа данные
    description: Optional[str] = None  # описание конкретного лота

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )  # создан
    updated_at: Optional[datetime] = None  # обновлен

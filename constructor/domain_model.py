from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
from datetime import datetime


class DealType(Enum):
    """Тип сделки."""
    RENT = 'rent'
    SALE = 'sale'


class ObjectType(Enum):
    """Тип объекта недвижимости."""
    FLAT = 'flat'
    HOUSE = 'house'
    ROOM = 'room'
    GARAGE = 'garage'
    COTTAGE = 'cottage'
    BED = 'bed'
    TOWNHOUSE = 'townhouse'
    COMMERCIAL = 'commercial'


class RentPeriod(Enum):
    """Период аренды."""
    DAILY = 'daily'
    MONTHLY = 'monthly'


class Currency(Enum):
    """Тип валюты."""
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'


@dataclass
class Phone:
    """Номер телефона."""
    country_code: str
    number: str


@dataclass
class Contacts:
    """Модель с суммарной контактной информацией."""
    phones: List[Phone] = field(default_factory=list)
    contact_email: Optional[str] = None
    owner_name: Optional[str] = None
    agent_name: Optional[str] = None


@dataclass
class Geo:
    """Координаты."""
    latitude: Optional[float] = None
    longitude: Optional[float] = None


@dataclass
class Underground:
    name: str
    id: Optional[int] = None
    time_minutes: Optional[int] = None
    transport_type: Optional[str] = None


@dataclass
class Address:
    """Модель с полной гео информацией."""
    country: Optional[str] = None
    region: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    street: Optional[str] = None
    house_number: Optional[str] = None
    block: Optional[str] = None
    apartment: Optional[str] = None
    geo: Optional[Geo] = None
    undergrounds: List[Underground] = field(default_factory=list)


@dataclass
class RentInfo:
    """Информация об аренде."""
    price: Optional[float] = None
    currency: Optional[Currency] = None
    period: Optional[RentPeriod] = None

    security_deposit: Optional[float] = None
    agent_fee_percent: Optional[float] = None
    utilities_included: Optional[bool] = None

    min_rent_term_months: Optional[int] = None


@dataclass
class Deal:
    """Модель с общей информацией о сделке."""
    deal_type: DealType
    rent: Optional[RentInfo] = None


@dataclass
class FlatDetails:
    """Информация по помещению."""
    rooms_count: Optional[int] = None

    total_area: Optional[float] = None
    living_area: Optional[float] = None
    kitchen_area: Optional[float] = None

    floor: Optional[int] = None
    floors_total: Optional[int] = None

    ceiling_height: Optional[float] = None

    balconies_count: Optional[int] = None
    loggias_count: Optional[int] = None

    repair_type: Optional[str] = None
    layout_type: Optional[str] = None


@dataclass
class BuildingDetails:
    """Информация по строению."""
    year_built: Optional[int] = None
    building_type: Optional[str] = None

    has_elevator: Optional[bool] = None
    has_parking: Optional[bool] = None
    has_garbage_chute: Optional[bool] = None


@dataclass
class Conditions:
    """Условия проживания."""
    pets_allowed: Optional[bool] = None
    children_allowed: Optional[bool] = None
    smoking_allowed: Optional[bool] = None

    furnished: Optional[bool] = None
    has_washer: Optional[bool] = None
    has_tv: Optional[bool] = None
    has_internet: Optional[bool] = None


@dataclass
class Photo:
    """Фото."""
    url: str
    is_default: bool = False


@dataclass
class Media:
    """Медиа данные объекта."""
    photos: List[Photo] = field(default_factory=list)
    videos: List[str] = field(default_factory=list)
    virtual_tour_url: Optional[str] = None


@dataclass
class RealtyObject:
    """Моедль с суммарной полной информацией по объекту недвижимости."""
    id: str

    object_type: ObjectType
    deal: Deal

    address: Optional[Address] = None
    flat: Optional[FlatDetails] = None
    building: Optional[BuildingDetails] = None

    conditions: Optional[Conditions] = None
    media: Optional[Media] = None
    contacts: Optional[Contacts] = None

    description: Optional[str] = None

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

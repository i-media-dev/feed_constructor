from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional


class DealType(Enum):
    """Тип сделки."""
    RENT = 'rent'  # аренда
    SALE = 'sale'  # продажа


class ObjectType(Enum):
    """Тип объекта недвижимости."""
    FLAT = 'flat'  # квартира
    HOUSE = 'house'  # дом
    ROOM = 'room'  # комната
    GARAGE = 'garage'  # гараж
    COTTAGE = 'cottage'  # коттедж
    BED = 'bed'  # койко-место
    TOWNHOUSE = 'townhouse'  # таунхаус
    COMMERCIAL = 'commercial'  # коммерческая
    DUPLEX = 'duplex'  # дюплекс
    LOT = 'lot'  # участок


class RentPeriod(Enum):
    """Период аренды."""
    DAILY = 'daily'  # по дням
    MONTHLY = 'monthly'  # по месяцам


class Currency(Enum):
    """Тип валюты."""
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'


# class Renovation(Enum):
#     """Тип ремонта."""
#     EUVRO = 'евроремонт'
#     COSMETIC = 'косметический'
#     DESIGNER = 'дизайнерский'
#     REPAIR = 'требует ремонта'


@dataclass
class Phone:
    """Номер телефона."""
    country_code: str  # телефонный код страны
    number: str  # номер телефона


@dataclass
class Contacts:
    """Модель с суммарной контактной информацией."""
    phones: List[Phone] = field(default_factory=list)  # номер телефона
    contact_email: Optional[str] = None  # почта
    owner_name: Optional[str] = None  # имя владельца
    agent_name: Optional[str] = None  # имя агента
    # право собственности (посредник, застройщик, владелец)
    property_rights: Optional[str] = None


@dataclass
class Geo:
    """Координаты."""
    latitude: Optional[float] = None  # широта
    longitude: Optional[float] = None  # долгота


@dataclass
class Underground:
    """Модель информации о метро."""
    name: str  # название
    id: Optional[int] = None  # айди (нужен для некоторых площадок)
    time_walk: Optional[int] = None  # время на путь до метро пешком
    time_transport: Optional[str] = None  # время на путь до метро транспорт


@dataclass
class Address:
    """Модель с полной гео информацией."""
    country: Optional[str] = None  # Страна
    region: Optional[str] = None  # Область
    city: Optional[str] = None  # Город
    district: Optional[str] = None  # Район
    street: Optional[str] = None  # Улица
    house_number: Optional[str] = None  # Номер дома
    block: Optional[str] = None  # Корпус
    apartment: Optional[str] = None  # Номер квартиры
    geo: Optional[Geo] = None  # Координаты
    undergrounds: List[Underground] = field(default_factory=list)  # Метро


@dataclass
class RentInfo:
    """Информация об аренде."""
    price: Optional[float] = None  # Цена
    currency: Optional[Currency] = None  # Валюта
    period: Optional[RentPeriod] = None  # Период

    security_deposit: Optional[float] = None  # залог
    agent_fee_percent: Optional[float] = None  # процент агентского взноса
    utilities_included: Optional[bool] = None  # включение коммунальных услуг

    min_rent_term_months: Optional[int] = None  # Минимальный срок аренды


@dataclass
class Deal:
    """Модель с общей информацией о сделке."""
    deal_type: DealType  # тип сделки (аренда, покупка)
    rent: Optional[RentInfo] = None  # информация об аренде


@dataclass
class FlatDetails:
    """Информация по помещению."""
    rooms_count: Optional[int] = None  # количество комнат

    total_area: Optional[float] = None  # общая площадь
    living_area: Optional[float] = None  # жилая площадь
    kitchen_area: Optional[float] = None  # площадь кухни

    floor: Optional[int] = None  # этаж
    floors_total: Optional[int] = None  # всего этажей

    ceiling_height: Optional[float] = None  # высота потолков

    balconies_count: Optional[int] = None  # количество балконов
    loggias_count: Optional[int] = None  # количество лоджий

    # repair_type: Optional[str] = None
    layout_type: Optional[str] = None  # тип макета


@dataclass
class BuildingDetails:
    """Информация по строению."""
    year_built: Optional[int] = None  # год постройки
    building_type: Optional[str] = None  # тип строения
    building_material: Optional[str] = None  # материал строения

    has_elevator: Optional[bool] = None  # лифт
    has_parking: Optional[bool] = None  # паркинг
    has_garbage_chute: Optional[bool] = None  # мусоропровод


@dataclass
class Conditions:
    """Условия проживания."""
    pets_allowed: Optional[bool] = None  # животные
    children_allowed: Optional[bool] = None  # дети
    smoking_allowed: Optional[bool] = None  # курение

    furnished: Optional[bool] = None  # мебель
    has_washer: Optional[bool] = None  # стиральная машина
    has_tv: Optional[bool] = None  # телевизор
    has_internet: Optional[bool] = None  # интернет

    renovation: Optional[str] = None  # тип ремонта


@dataclass
class Photo:
    """Фото."""
    url: str  # ссылка на фото
    is_default: bool = False  # использовать фото по умолчанию


@dataclass
class Media:
    """Медиа данные объекта."""
    photos: List[Photo] = field(default_factory=list)  # фото
    videos: List[str] = field(default_factory=list)  # видео
    virtual_tour_url: Optional[str] = None  # виртуальный тур


@dataclass
class RealtyObject:
    """Моедль с суммарной полной информацией по объекту недвижимости."""
    id: str  # айди объекта

    object_type: ObjectType  # тип объекта
    deal: Deal  # тип сделки

    address: Optional[Address] = None  # адрес
    flat: Optional[FlatDetails] = None  # информация по квартире
    building: Optional[BuildingDetails] = None  # информация по зданию

    conditions: Optional[Conditions] = None  # условия проживания
    media: Optional[Media] = None  # все медиа для объекта
    contacts: Optional[Contacts] = None  # контактные данные

    description: Optional[str] = None  # описание

    created_at: Optional[datetime] = None  # когда создано
    updated_at: Optional[datetime] = None  # когда обновлено

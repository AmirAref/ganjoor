from pydantic import BaseModel, Field, TypeAdapter
from uuid import UUID

from datetime import datetime


class RImage(BaseModel):
    id: UUID = Field(None, description="Id")
    originalFileName: str = Field(None, description="Original File Name")
    contentType: str = Field(None, description="content type")
    fileSizeInBytes: int = Field(None, description="Original Image File Size In Byte")
    imageWidth: int = Field(None, description="Original Image Width")
    imageHeight: int = Field(None, description="Original Image Height")
    folderName: str = Field(
        None,
        description="پوشه محل ذخیره تصویر",
    )
    storedFileName: str = Field(
        None,
        description="نام فایل ذخیره شده با بالاترین کیفیت",
    )
    dataTime: datetime = Field(None, description="datetime")
    lastModified: datetime = Field(
        None, description="Last Modified for caching purposes"
    )


class GeoLocation(BaseModel):
    id: int = Field(None, description="id")
    name: str = Field(None, description="name")
    latitude: float = Field(None, description="Latitude")
    longitude: float = Field(None, description="Longitude")


class Poet(BaseModel):
    id: int = Field(None, description="id")
    name: str = Field(None, description="name")
    description: str | None = Field(None, description="description")
    nickname: str = Field(None, description="short name")
    rImage: RImage | None = None
    rImageId: UUID = Field(None, description="user image id")
    published: bool = Field(None, description="published on website")
    birthYearInLHijri: int = Field(None, description="birth year in lunar hijri")
    deathYearInLHijri: int = Field(None, description="death year in lunar hijri")
    pinOrder: int = Field(
        None, description="Home page pin order (zero means not pinned)"
    )
    validBirthDate: bool = Field(
        None,
        description="BirthYearInLHijri, for some poets it is only indicator of their century of birth and should not be relied as their valid birth date",
    )
    validDeathDate: bool = Field(
        None,
        description="DeathYearInLHijri, for some poets it is only indicator of their century of death and should not be relied as their valid death date",
    )
    birthLocationId: int = Field(None, description="birth location id")
    birthLocation: GeoLocation | None = None
    deathLocationId: int = Field(None, description="death location id")
    deathLocation: GeoLocation | None = None


PoetsTypeAdapter = TypeAdapter(list[Poet])

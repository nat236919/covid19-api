"""
FILE: covid_api_v2_model.py
DESCRIPTION: Models for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List, Optional

from pydantic import BaseModel


#######################################
# CurrentModel
#######################################
class CurrentModel(BaseModel):
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int


#######################################
# CurrentUSModel
#######################################
class CurrentUSModel(BaseModel):
    province_state: str
    confirmed: int
    deaths: int
    recovered: int
    active: int


#######################################
# CountryModel
#######################################
class CurrentCountryModel(BaseModel):
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int


#######################################
# TimeseriesGlobalModel
#######################################
class TimeseriesGlobalModel(BaseModel):
    confirmed: int
    deaths: int
    recovered: int


#######################################
# TimeseriesCaseModel
#######################################

class TimeseriesCaseCoordinatesModel(BaseModel):
    Lat: float
    Long: float


class TimeseriesCaseDataModel(BaseModel):
    date: str
    value: int


class TimeseriesUSInfoModel(BaseModel):
    UID: str
    iso2: str
    iso3: str
    code3: str
    FIPS: str
    Admin2: str


class TimeseriesCaseModel(BaseModel):
    Province_State: str
    Country_Region: str
    Coordinates: TimeseriesCaseCoordinatesModel
    Info: Optional[TimeseriesUSInfoModel]
    TimeSeries: List[TimeseriesCaseDataModel]


class TimeseriesUSInfoBuilder:
    UID: Optional[str] = None
    iso2: Optional[str] = None
    iso3: Optional[str] = None
    code3: Optional[str] = None
    FIPS: Optional[str] = None
    Admin2: Optional[str] = None

    def is_valid_build(self) -> bool:
        return (
                isinstance(self.UID, str) and
                isinstance(self.iso2, str) and
                isinstance(self.iso3, str) and
                isinstance(self.code3, str) and
                isinstance(self.FIPS, str) and
                isinstance(self.Admin2, str)
        )

    def set_UID(self, value: str) -> 'TimeseriesUSInfoBuilder':
        self.UID = value
        return self

    def set_iso2(self, value: str) -> 'TimeseriesUSInfoBuilder':
        self.iso2 = value
        return self

    def set_iso3(self, value: str) -> 'TimeseriesUSInfoBuilder':
        self.iso3 = value
        return self

    def set_code3(self, value: str) -> 'TimeseriesUSInfoBuilder':
        self.code3 = value
        return self

    def set_FIPS(self, value: str) -> 'TimeseriesUSInfoBuilder':
        self.FIPS = value
        return self

    def set_Admin2(self, value: str) -> 'TimeseriesUSInfoBuilder':
        self.Admin2 = value
        return self

    def build(self) -> TimeseriesUSInfoModel:
        if not self.is_valid_build():
            raise ValueError("Builder has missing required fields")

        return TimeseriesUSInfoModel(
            UID=self.UID,
            iso2=self.iso2,
            iso3=self.iso3,
            code3=self.code3,
            FIPS=self.FIPS,
            Admin2=self.Admin2
        )


class TimeseriesBuilder:
    Province_State: Optional[str] = None
    Country_Region: Optional[str] = None
    Coordinates: Optional[TimeseriesCaseCoordinatesModel] = None
    Info: Optional[TimeseriesUSInfoBuilder] = None
    TimeSeries: List[TimeseriesCaseDataModel]

    is_info_required: bool

    def __init__(self, is_info_required: bool = False):
        self.is_info_required = is_info_required
        self.TimeSeries = []

    def set_info(self) -> TimeseriesUSInfoBuilder:
        info = TimeseriesUSInfoBuilder()
        self.Info = info
        return info

    def set_province_state(self, name: str) -> 'TimeseriesBuilder':
        self.Province_State = name
        return self

    def set_country_region(self, name: str) -> 'TimeseriesBuilder':
        self.Country_Region = name
        return self

    def set_coordinates(self, lat: float, long: float) -> 'TimeseriesBuilder':
        coord = TimeseriesCaseCoordinatesModel(
            Lat=lat,
            Long=long
        )
        self.Coordinates = coord
        return self

    def add_data(self, date: str, value: int) -> 'TimeseriesBuilder':
        data = TimeseriesCaseDataModel(
            date=date,
            value=value
        )
        self.TimeSeries.append(data)
        return self

    def _info_is_valid_build(self) -> bool:
        return (
            (isinstance(self.Info, TimeseriesUSInfoBuilder) and self.Info.is_valid_build())
            or (self.Info is None and not self.is_info_required)
        )

    def is_valid_build(self) -> bool:
        return (
                isinstance(self.Province_State, str)
                and isinstance(self.Country_Region, str)
                and isinstance(self.Coordinates, TimeseriesCaseCoordinatesModel)
                and self._info_is_valid_build()
        )

    def build(self) -> TimeseriesCaseModel:
        if not self.is_valid_build():
            raise ValueError("Builder has invalid or missing required fields.")

        return TimeseriesCaseModel(
            Province_State=self.Province_State,
            Country_Region=self.Country_Region,
            Info=self.Info.build() if self.Info is not None else None,
            Coordinates=self.Coordinates,
            TimeSeries=self.TimeSeries
        )

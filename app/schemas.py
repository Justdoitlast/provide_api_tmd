from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class tmd_apiSchema(BaseModel):
    wmostationnumber: Optional[str] = None
    stationnamethai: Optional[str] = None
    stationnameenglish: Optional[str] = None
    province: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    observation: Optional[str] = None
    datetime: Optional[str] = None
    meansealevelpressure: Optional[float] = None
    temperature: Optional[float] = None
    maxtemperature: Optional[float] = None
    differentfrommaxtemperature: Optional[float] = None
    mintemperature: Optional[float] = None
    differentfrommintemperature: Optional[float] = None
    relativehumidity: Optional[float] = None
    winddirection: Optional[str] = None
    windspeed: Optional[float] = None
    rainfall: Optional[float] = None
    id: Optional[int] = None

   
    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class Requesttmd_api(BaseModel):
    parameter: tmd_apiSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
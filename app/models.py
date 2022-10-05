from sqlalchemy import  Column, Integer, String, Numeric
from config import Base

class tmd_api(Base):
    __tablename__ ="dupe_tmd_api"

    wmostationnumber = Column(String)
    stationnamethai = Column(String)
    stationnameenglish = Column(String)
    province = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    observation = Column(String)
    datetime = Column(String)
    meansealevelpressure = Column(Numeric)
    temperature = Column(Numeric)
    maxtemperature = Column(Numeric)
    differentfrommaxtemperature = Column(Numeric)
    mintemperature = Column(Numeric)
    differentfrommintemperature = Column(Numeric)
    relativehumidity = Column(Numeric)
    winddirection = Column(String)
    windspeed = Column(Numeric)
    rainfall = Column(Numeric)
    id = Column(Integer, primary_key=True, index=True)




from sqlalchemy.orm import Session
from models import tmd_api
from schemas import tmd_apiSchema


def get_tmd(db: Session, limit: int = 100):
    return db.query(tmd_api).limit(limit).all()


def get_tmd_api_by_station(db: Session, tmd_api_station: str):
    return db.query(tmd_api).filter(tmd_api.id == tmd_api_station).all()


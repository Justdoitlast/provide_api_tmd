from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import tmd_apiSchema, Request, Response, Requesttmd_api

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_tmd(limit: int = 100, db: Session = Depends(get_db)):
    _tmd = crud.get_tmd(db, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_tmd)



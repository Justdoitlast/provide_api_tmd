from fastapi import FastAPI
import models
from routes import router
from config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def Home():
    return "hello World"
    
app.include_router(router, prefix="/tmd", tags=["dupe_tmd_api"])

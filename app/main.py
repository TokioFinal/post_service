from typing import Annotated
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.database.config import create_db_and_tables
from app.routers import posts


app = FastAPI()
app.include_router(posts.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get('/healthz')
def healthz():
    return JSONResponse( status_code=200 ,content = {"message": "Everything okay"})
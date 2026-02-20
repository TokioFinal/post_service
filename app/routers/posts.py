from typing import Annotated
from fastapi import APIRouter, Depends
from app.database.config import get_session
from app.models.post import PostCreate
from app.dependencies import verify_token
from sqlmodel import  Session
from fastapi.responses import JSONResponse

SessionDep = Annotated[Session, Depends(get_session)]
router = APIRouter()

@router.post("/post")
def create_post(session: SessionDep, data: PostCreate, author: str = Depends(verify_token)):
    
    return 

@router.get("/posts")
def create_post(session: SessionDep, data: PostCreate, author: str = Depends(verify_token)):
    return JSONResponse(status_code=200, content= {"nice":"you are authenticated"})

@router.delete("/posts")
def create_post(session: SessionDep, data: PostCreate, author: str = Depends(verify_token)):
    return JSONResponse(status_code=200, content= {"nice":"you are authenticated"})

@router.update("/posts")
def create_post(session: SessionDep, data: PostCreate, author: str = Depends(verify_token)):
    return JSONResponse(status_code=200, content= {"nice":"you are authenticated"})
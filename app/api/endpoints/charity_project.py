from fastapi import APIRouter, Depends

from app.crud.charity_project import create_charity_project
from app.schemas.charity_project import CharityProjectCreate

router = APIRouter()


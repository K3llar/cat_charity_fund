from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.charity_project import (create_charity_project,
                                      get_project_id_by_name,
                                      get_all_charity_projects_from_db)
from app.schemas.charity_project import CharityProjectCreate, CharityProjectDB

router = APIRouter()


@router.post('/',
             response_model=CharityProjectDB,
             response_model_exclude_none=True)
async def create_new_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)
):
    project_id = await get_project_id_by_name(charity_project.name,
                                              session)
    if project_id:
        raise HTTPException(
           status_code=422,
           detail='Проект с таким названием уже существует!'
        )
    new_project = await create_charity_project(charity_project,
                                               session)
    return new_project


@router.get('/',
            response_model=list[CharityProjectDB],
            response_model_exclude_none=True,)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session)
):
    all_projects = await get_all_charity_projects_from_db(session)
    return all_projects


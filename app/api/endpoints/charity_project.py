from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.charity_project import (create_charity_project,
                                      get_project_id_by_name,
                                      get_all_charity_projects_from_db,
                                      update_charity_project,
                                      delete_charity_project)
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectUpdate,
                                         CharityProjectDB)
from app.api.validators import (check_name_duplicate,
                                check_charity_project_before_edit,
                                check_charity_project_exists,
                                check_charity_project_invested_amount)

router = APIRouter()


@router.post('/',
             response_model=CharityProjectDB,
             response_model_exclude_none=True)
async def create_new_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)
):
    await check_name_duplicate(charity_project.name, session)
    new_project = await create_charity_project(charity_project,
                                               session)
    return new_project


@router.get('/',
            response_model=list[CharityProjectDB],
            response_model_exclude_none=True, )
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session)
):
    all_projects = await get_all_charity_projects_from_db(session)
    return all_projects


@router.patch('/{charity_project_id}',
              response_model=CharityProjectDB,
              response_model_exclude_none=True, )
async def partially_update_charity_project(
        charity_project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    charity_project = await check_charity_project_before_edit(
        charity_project_id, session
    )

    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)

    if obj_in.full_amount is not None:
        if obj_in.full_amount <= charity_project.invested_amount:
            raise HTTPException(
                status_code=422,
                detail='Нельзя внести сумму меньше текущей!'
            )

    charity_project = await update_charity_project(
        charity_project, obj_in, session
    )
    return charity_project


@router.delete('/{charity_project_id}',
               response_model=CharityProjectDB,
               response_model_exclude_none=True)
async def remove_charity_project(
        charity_project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    await check_charity_project_invested_amount(
        charity_project_id, session
    )
    charity_project = await delete_charity_project(
        charity_project, session
    )
    return charity_project

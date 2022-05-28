from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.crud.charity_project import (get_project_id_by_name,
                                      get_charity_project_by_id)


async def check_name_duplicate(
        charity_project_name: str,
        session: AsyncSession,
) -> None:
    project_id = await get_project_id_by_name(charity_project_name,
                                              session)
    if project_id:
        raise HTTPException(
            status_code=422,
            detail='Проект с таким названием уже существует!'
        )


async def check_charity_project_exists(
        charity_project_id: int,
        session: AsyncSession
) -> CharityProject:
    charity_project = await get_charity_project_by_id(
        charity_project_id, session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден'
        )
    return charity_project


async def check_charity_project_before_edit(
        charity_project_id: int,
        session: AsyncSession
) -> CharityProject:
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    return charity_project


# async def check_fields_in_dict(
#         dictionary: dict,
# ):
#     for field in dictionary:
#         if dictionary[field] is None:
#             raise HTTPException(
#                 status_code=422,
#                 detail=f'Поле {field} не может быть пустым'
#             )


async def check_charity_project_invested_amount(
        charity_project_id: int,
        session: AsyncSession
):
    charity_project = await get_charity_project_by_id(
        charity_project_id, session
    )
    if charity_project.invested_amount != 0:
        raise HTTPException(
            status_code=422,
            detail='Нельзя удалить проект с начавшимся сбором средств!'
        )
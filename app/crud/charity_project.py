from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.models.charity_project import CharityProject
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectUpdate)


async def create_charity_project(
        new_project: CharityProjectCreate,
        session: AsyncSession,
) -> CharityProject:
    new_project_data = new_project.dict()
    db_project = CharityProject(**new_project_data)
    session.add(db_project)
    await session.commit()
    await session.refresh(db_project)
    return db_project


async def get_project_id_by_name(
        project_name: str,
        session: AsyncSession,
) -> Optional[int]:
    db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
    db_project_id = db_project_id.scalars().first()
    return db_project_id


async def get_all_charity_projects_from_db(
        session: AsyncSession
) -> list[CharityProject]:
    all_projects = await session.execute(select(CharityProject))
    all_projects = all_projects.scalars().all()
    return all_projects


async def get_charity_project_by_id(
        charity_project_id: int,
        session: AsyncSession,
) -> Optional[CharityProject]:
    db_project = await session.get(CharityProject,
                                   charity_project_id)
    return db_project


async def update_charity_project(
        db_project: CharityProject,
        project_in: CharityProjectUpdate,
        session: AsyncSession,
) -> CharityProject:
    obj_data = jsonable_encoder(db_project)
    update_data = project_in.dict(exclude_unset=True)
    for field in update_data:
        if update_data[field] is None:
            raise HTTPException(
                status_code=422,
                detail=f'Поле {field} не может быть пустым!'
            )
    for field in obj_data:
        if field in update_data:
            setattr(db_project, field, update_data[field])
    session.add(db_project)
    await session.commit()
    await session.refresh(db_project)
    return db_project


async def delete_charity_project(
        db_project: CharityProject,
        session: AsyncSession,
) -> CharityProject:
    await session.delete(db_project)
    await session.commit()
    return db_project

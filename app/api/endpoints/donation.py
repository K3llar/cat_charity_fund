from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.crud.donation import (create_donation,
                               get_all_donations_from_db,
                               get_all_donations_by_user)
from app.schemas.donation import DonationCreate, DonationDB
from app.schemas.user import UserDB
from app.services.invest import check_charity_projects_for_investing


router = APIRouter()


@router.post('/',
             response_model=DonationDB,
             response_model_exclude_none=True,)
async def create_new_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: UserDB = Depends(current_user)
):
    new_donation = await create_donation(
        donation, session, user
    )
    new_donation = await check_charity_projects_for_investing(new_donation, session)
    return new_donation


@router.get('/',
            response_model=list[DonationDB],
            response_model_exclude_none=True,
            dependencies=[Depends(current_superuser)])
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session)
):
    all_donations = await get_all_donations_from_db(session)
    return all_donations


@router.get('/my',
            response_model=list[DonationDB],
            response_model_exclude={'user_id'})
async def get_my_donations(
        session: AsyncSession = Depends(get_async_session),
        user: UserDB = Depends(current_user),
):
    """Получение списка всех пожертвований для текущего пользователя"""
    donations = await get_all_donations_by_user(
        session=session, user=user
    )
    return donations

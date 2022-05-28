from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.donation import (create_donation,
                               get_all_donations_from_db)
from app.schemas.donation import DonationCreate, DonationDB
from app.services.invest import check_charity_projects_for_investing


router = APIRouter()


@router.post('/',
             response_model=DonationDB,
             response_model_exclude_none=True)
async def create_new_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session)
):
    new_donation = await create_donation(
        donation, session
    )
    new_donation = await check_charity_projects_for_investing(new_donation, session)
    return new_donation


@router.get('/',
            response_model=list[DonationDB],
            response_model_exclude_none=True)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session)
):
    all_donations = await get_all_donations_from_db(session)
    return all_donations



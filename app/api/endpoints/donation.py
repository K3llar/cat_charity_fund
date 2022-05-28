from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.donation import (create_donation)
from app.schemas.donation import DonationCreate, DonationDB


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
    return new_donation


